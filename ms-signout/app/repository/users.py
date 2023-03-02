from app.config import commit_rollback, db
from app.model.users import Users
from app.repository.base import BaseRepo
from sqlalchemy.future import select


class UsersRepository(BaseRepo):
    model = Users

    @staticmethod
    async def find_by_username(username: str):
        try:
            query = select(Users).where(Users.username == username)
            print('query', query)
            return (await db.execute(query)).scalar_one_or_none()
        except Exception as e:
            print('error', e)
            return None
