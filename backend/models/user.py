from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.database.base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]

    messages: Mapped[List["Message"]] = relationship("Message", back_populates="user")
