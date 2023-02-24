from pydantic import BaseModel
from app.api.db.models import Auction


class AuctionSchema(BaseModel):
    id: int
    title: str
    description: str
    place: str
    date: str


# async def auction_orm_to_schema(auction: Auction):
#     result = AuctionSchema(
#         id=auction.id,
#         place=auction.place,
#         date=str(auction.date))

