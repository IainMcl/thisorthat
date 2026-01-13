from fastapi import APIRouter
from options.schemas import Option

router = APIRouter(prefix="/options")


@router.get("/", tags=["options"])
async def get_options() -> list[Option]:
    return [
        Option(
            id=1,
            name="Option 1",
            image_url="http://example.com/image1.png",
            metadata={"key1": "value1"},
        ),
        Option(
            id=2,
            name="Option 2",
            image_url="http://example.com/image2.png",
            metadata={"key2": "value2"},
        ),
    ]
