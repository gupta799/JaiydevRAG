from flask import current_app
import redis
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def runPreProcessing():
    client = redis.StrictRedis(
    host=current_app.config['REDIS_HOST'],
    port=current_app.config['REDIS_PORT'],
    password=current_app.config['REDIS_PASSWORD'],
    decode_responses=True
    )
    return client

def getModel():
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    return embed_model
