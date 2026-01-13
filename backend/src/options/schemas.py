from pydantic import BaseModel, Field


class Option(BaseModel):
    id: int = Field(..., description="The unique identifier of the option")
    name: str = Field(..., description="The name of the option")
    image_url: str = Field(..., description="The URL of the option's image")
    metadata: dict = Field(..., description="Additional metadata for the option")
