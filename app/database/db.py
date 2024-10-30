from elasticsearch_dsl import async_connections
from elasticsearch import AsyncElasticsearch


class ElasticSearchClient:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            # Generar instancia de ElasticSearch
            async_connections.create_connection(hosts=["http://localhost:9200"])
            cls._instace = async_connections.get_connection()

        return cls._instance


def get_instance():
    instance = ElasticSearchClient.get_instance
    return instance
