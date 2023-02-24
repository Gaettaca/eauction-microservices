from app.api.db.base import engine, get_session
from app.api.db.models import Auction
from app.api.schemas import AuctionSchema
from sqlalchemy.future import select


async def get_all_auctions() -> list[AuctionSchema]:
    async with get_session() as session:
        result = await session.execute(select(Auction))

        auctions = []
        for auction in result.scalars():
            schema = AuctionSchema(
                id=auction.id,
                title=auction.title,
                description=auction.description[:100]+"...",
                place=auction.place,
                date=str(auction.date)
            )
            auctions.append(schema)
    return auctions


async def get_auction_by_id(auction_id: int) -> AuctionSchema:
    async with get_session() as session:
        result = await session.execute(select(Auction).where(Auction.id == auction_id))

        for auction in result.scalars():
            schema = AuctionSchema(
                id=auction.id,
                title=auction.title,
                description=auction.description,
                place=auction.place,
                date=str(auction.date)
            )
    return schema
