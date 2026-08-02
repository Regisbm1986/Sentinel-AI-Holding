from .jwt_manager import validate_token
from .exceptions import AuthError

def require_auth(token: str):
    try:
        payload = validate_token(token)
        return payload
    except Exception as e:
        raise AuthError(str(e))
