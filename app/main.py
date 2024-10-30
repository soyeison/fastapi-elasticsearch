from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from elasticsearch_dsl import (
    async_connections,
    AsyncDocument,
    Text,
    Keyword,
    AsyncSearch,
    mapped_field,
    Search,
)
from elasticsearch import AsyncElasticsearch

app = FastAPI()


async def get_elasticsearch():
    return async_connections.create_connection(hosts=["http://localhost:9200"])


class User(AsyncDocument):
    first_name: str = mapped_field(Text(fields={"raw": Keyword()}))
    last_name: str = mapped_field(Text(analyzer="snowball"))

    class Index:
        name = "user"


@app.get("/")
async def root():
    await User()
    return JSONResponse(content="Hola Mundo", status_code=200)


@app.post("/user")
async def create_document(es: AsyncElasticsearch = Depends(get_elasticsearch)):
    try:
        await User(first_name="Jhon", last_name="Doe").save()
        return JSONResponse(content="Melo", status_code=201)
    finally:
        await es.close()


@app.get("/user")
async def get_user(es: AsyncElasticsearch = Depends(get_elasticsearch)):
    try:
        """user = await User.get(id="xa-O35IBwldJOWK-xvVC")
        print("User:", user.first_name)
        print("User:", user.last_name)"""

        s = User.search()
        s.from_dict({"query": {"bool": {"must": {"match": {"first_name": "Jhon"}}}}})
        response = await s.execute()
        print(response)
        for hit in response:
            print(hit.meta["id"])
            print(hit.first_name)
            print(hit.last_name)
        """ s = (
            await AsyncSearch()
            .index("user")
            .from_dict({"query": {"terms": {"_id": ["xa-O35IBwldJOWK-xvVC"]}}})
            .execute()
        )
        print("S: ", s) """
        return JSONResponse(content="Melo", status_code=200)
    finally:
        await es.close()
