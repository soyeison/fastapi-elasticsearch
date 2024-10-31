from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from elasticsearch_dsl import async_connections
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreateSchema

app = FastAPI()


@app.get("/")
async def root():
    return JSONResponse(content="Hola Mundo", status_code=200)


@app.post("/user")
async def create_user(
    user_payload: UserCreateSchema,
    user_service: UserService = Depends(UserService),
):
    user_created = await user_service.create_user(user_payload=user_payload)
    print("User created: ", user_created)
    return JSONResponse(content="Melo", status_code=201)


@app.get("/user")
async def get_user(
    user_id: str,
    user_service: UserService = Depends(UserService),
):
    """user = await User.get(id="xa-O35IBwldJOWK-xvVC")
    print("User:", user.first_name)
    print("User:", user.last_name)"""

    """ s = User.search()
        s.from_dict({"query": {"bool": {"must": {"match": {"first_name": "Jhon"}}}}})
        response = await s.execute()
        print(response)
        for hit in response:
            print(hit.meta["id"])
            print(hit.first_name)
            print(hit.last_name) """
    """ s = (
            await AsyncSearch()
            .index("user")
            .from_dict({"query": {"terms": {"_id": ["xa-O35IBwldJOWK-xvVC"]}}})
            .execute()
        )
        print("S: ", s) """
    user = await user_service.get_user_by_id(user_id=user_id)
    return JSONResponse(content=user, status_code=200)
