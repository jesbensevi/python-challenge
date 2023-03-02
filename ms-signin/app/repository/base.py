from typing import Generic, TypeVar

from app.config import commit_rollback, db
from sqlalchemy.future import select

T = TypeVar('T')


class BaseRepo:
    model = Generic[T]

    @classmethod
    async def get_by_id(cls, model_id: str):
        query = select(cls.model).where(cls.model.id == model_id)
        return (await db.execute(query)).scalar_one_or_none()
