from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from models import City, Temperature

async def get_cities(session: AsyncSession) -> List[City]:
    result = await session.execute(select(City))
    return result.scalars().all()


async def get_temperatures(session: AsyncSession) -> List[Temperature]:
    result = await session.execute(select(Temperature))
    return result.scalars().all()
