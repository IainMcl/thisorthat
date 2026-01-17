from sqlmodel import Field, SQLModel, JSON, Column


class Option(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    image_url: str | None = None
    meta: dict = Field(default_factory=dict, sa_column=Column(JSON))
