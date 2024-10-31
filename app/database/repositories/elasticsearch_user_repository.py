from elasticsearch import AsyncElasticsearch
from fastapi import Depends
from app.database.db import connect_to_elasticsearch
from app.database.models.user_model import UserModel, PhoneModel
from app.schemas.user_schema import UserCreateSchema


class ElasticSearchUserRepository:
    def __init__(self, es: AsyncElasticsearch = Depends(connect_to_elasticsearch)):
        self.es_client = es

    async def create(self, user_paylod: UserCreateSchema):
        try:
            return await UserModel(
                first_name=user_paylod.first_name,
                last_name=user_paylod.last_name,
                phone=PhoneModel(
                    dial_code=user_paylod.phone_dial_code,
                    number=user_paylod.phone_number,
                    imei=None,
                ),
            ).save()
        finally:
            await self.es_client.close()

    async def get_user_by_id(self, user_id: str):
        try:
            return await UserModel.get(id=user_id)
        finally:
            await self.es_client.close()
