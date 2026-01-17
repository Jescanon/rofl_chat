from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, TEXT, CheckConstraint
from backend.database.base import Base


class Message(Base):
    __tablename__ = "message"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), index=True)
    role: Mapped[str] = mapped_column(default="user")
    content: Mapped[str] = mapped_column(TEXT)

    user: Mapped["User"] = relationship("User", back_populates="messages")

    __table_args__ = (
        CheckConstraint("role IN ('user', 'assistant')", name="message_role_check"),
    )