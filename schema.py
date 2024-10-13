from redis.commands.search.field import TextField, VectorField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from Indexer import VECTOR_DIMENSION, client
schema = (
    TextField("$.chunk", no_stem=True, as_name="chunk"),
    TextField("$.metaData.source", no_stem=True, as_name="source"),
    VectorField(
        "$.embedding",
        "FLAT",
        {
            "TYPE": "FLOAT32",
            "DIM": VECTOR_DIMENSION,
            "DISTANCE_METRIC": "COSINE",
        },
        as_name="embedding_vector",
    ),
)

definition = IndexDefinition(prefix=["RagStore:"], index_type=IndexType.JSON)

# Create index
res = client.ft("idx:RagStore_vss").create_index(
    fields=schema, definition=definition
)
