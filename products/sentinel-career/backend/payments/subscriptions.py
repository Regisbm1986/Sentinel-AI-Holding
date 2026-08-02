import uuid
from datetime import datetime, timedelta
from .models import Subscription
from .storage import JSONStorage
from .exceptions import SubscriptionError

storage = JSONStorage("subscriptions.json")

def create_subscription(user_id: str, plan: str):
    now = datetime.utcnow()
    end = now + timedelta(days=30)
    sub = Subscription(str(uuid.uuid4()), user_id, plan, "ACTIVE", now.isoformat(), end.isoformat())
    storage.save(sub.to_dict())
    return sub

def cancel_subscription(subscription_id: str):
    data = storage.load_all()
    for sub in data:
        if sub["id"] == subscription_id:
            sub["status"] = "CANCELED"
            storage.overwrite(data)
            return True
    raise SubscriptionError("Subscription not found")

def renew_subscription(subscription_id: str):
    data = storage.load_all()
    for sub in data:
        if sub["id"] == subscription_id:
            if sub["status"] != "ACTIVE":
                raise SubscriptionError("Only ACTIVE subs can renew")
            now = datetime.utcnow()
            end = now + timedelta(days=30)
            sub["started_at"] = now.isoformat()
            sub["expires_at"] = end.isoformat()
            storage.overwrite(data)
            return True
    raise SubscriptionError("Subscription not found")

def get_subscription(subscription_id: str):
    data = storage.load_all()
    for sub in data:
        if sub["id"] == subscription_id:
            return sub
    raise SubscriptionError("Subscription not found")
