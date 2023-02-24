from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
import sqlalchemy as sa

import asyncio
from app.api.db import config

from app.api.db.models import Base, Auction, Item, User, Lots, LotsItemsRelation

engine = create_async_engine(
    config.DATABASE_URL,
    echo=False,
    future=True,
)


def async_session_generator():
    return sessionmaker(
        engine, class_=AsyncSession
    )


@asynccontextmanager
async def get_session():
    try:
        async_session = async_session_generator()

        async with async_session() as session:
            yield session
    except:
        await session.rollback()
        raise
    finally:
        await session.close()
