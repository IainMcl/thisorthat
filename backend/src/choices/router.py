from fastapi import APIRouter

from choices.schemas import ChoiceSchema

router = APIRouter(prefix="/choices")


@router.post("/", tags=["choices"], status_code=201)
async def post_choice(choice: ChoiceSchema) -> None:
    pass
