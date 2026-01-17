from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.service.auth import hash_password, verify_password, create_access_token
from backend.database.sesion import get_async_db
from backend.schems.user import UserCreate
from backend.models.user import User as UserModel

from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=["registration"],
)

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def registration(newuser: UserCreate, db: AsyncSession = Depends(get_async_db)):
    info = await db.scalars(
        select(UserModel)
        .where(UserModel.username == newuser.username)
    )

    if info.first():
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Username already registered")

    new_user = UserModel(
        username=newuser.username,
        hashed_password=hash_password(newuser.password),
    )
    db.add(new_user)
    await db.commit()

    return {"message": f"User {new_user.username} registered successfully"}

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                db: AsyncSession = Depends(get_async_db)):

    result = await db.scalars(
        select(UserModel)
        .where(UserModel.username == form_data.username)
    )
    user = result.first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username, "id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}