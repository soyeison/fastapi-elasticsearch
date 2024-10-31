import json
from fastapi import Depends
from app.database.repositories.elasticsearch_user_repository import (
    ElasticSearchUserRepository,
)
from app.schemas.user_schema import UserCreateSchema


class UserService:
    def __init__(
        self,
        user_repository: ElasticSearchUserRepository = Depends(
            ElasticSearchUserRepository
        ),
    ):
        self.user_repo = user_repository

    async def create_user(self, user_payload: UserCreateSchema):
        user = await self.user_repo.create(user_paylod=user_payload)
        return user

    async def get_user_by_id(self, user_id: str):
        user = await self.user_repo.get_user_by_id(user_id=user_id)

        user = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "imei": user.phone.imei,
        }

        return user
