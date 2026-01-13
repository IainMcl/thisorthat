from sqlmodel import Field, SQLModel
from datetime import datetime, timezone


class UserChoice(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    chosen_option_id: int = Field(foreign_key="option.id")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class PresentedChoice(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_choice_id: int = Field(foreign_key="user.id")
    option_id: int = Field(foreign_key="option.id")
