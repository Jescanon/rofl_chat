from fastapi import Depends, APIRouter
from backend.schems.user import User as UserSchema
from backend.models.user import User

from backend.service.auth import get_current_user

router = APIRouter()

@router.get("/users/me", response_model=UserSchema)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user