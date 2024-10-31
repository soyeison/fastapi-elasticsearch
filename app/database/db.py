from elasticsearch_dsl import async_connections


async def connect_to_elasticsearch():
    return async_connections.create_connection(hosts=["http://localhost:9200"])
