from .exceptions import PaymentError

def validate_plan_id(plan_id):
    if plan_id not in {"free","pro","premium","master"}:
        raise PaymentError("Plano inválido")
