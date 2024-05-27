import numpy as np
from redis.commands.search.query import Query
from Indexer import client,embed_model
query = (
    Query('(*)=>[KNN 3 @embedding_vector $query_vector AS vector_score]')
    .sort_by('vector_score')
    .return_fields('vector_score', 'chunk', 'metaData.source')
    .dialect(2)
)
query_vector = embed_model.get_text_embedding("professional experience at Visa Inc.")
# Execute the query
query_vector_bytes = np.array(query_vector, dtype=np.float32).tobytes()
params = {"query_vector": query_vector_bytes}

result = client.ft("idx:RagStore_vss").search(query, query_params=params)
print(result)