from pydantic import BaseModel, Field


class ChoiceSchema(BaseModel):
    user_id: int = Field(..., description="The ID of the user making the choice")
    presented_option_ids: list[int] = Field(
        ..., description="List of presented option IDs"
    )
    chose_option_id: int = Field(
        ..., description="The ID of the option that was chosen"
    )
