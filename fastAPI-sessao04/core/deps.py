from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import Session



async def get_session() -> Generator:
    session: AsyncSession = Session()

    # deixa a conexão aberta para uso, e no fim encerra
    try:
        yield session
    finally:
        await session.close()