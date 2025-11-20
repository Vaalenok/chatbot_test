import enum
import uuid
from sqlalchemy import BigInteger, Enum, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.db.database import Base


class Author(str, enum.Enum):
    USER = "user"
    ASSISTANT = "assistant"


class User(Base):
    __tablename__ = "users"

    tg_id: Mapped[int] = mapped_column(BigInteger)
    message_history: Mapped[list["Message"]] = relationship(
        "Message", back_populates="user", cascade="all, delete-orphan", lazy="selectin"
    )


class Message(Base):
    __tablename__ = "messages"

    author: Mapped[Author] = mapped_column(Enum(Author, name="author_enum"))
    content: Mapped[str] = mapped_column()

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    user: Mapped["User"] = relationship("User", back_populates="message_history")
