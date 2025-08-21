import os
from pymongo import MongoClient

# A URI de conexão com o MongoDB Atlas deve ser a mesma do seu main.py
mongo_uri = "mongodb+srv://cardoneluisfelipe08:cardoneregim@cluster0.rzcpwpu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(mongo_uri)
db = client['ecossistema_uberlandia']
collection = db['empresas']

# Cria um índice de texto no campo 'razao_social'
print("Criando o índice de texto no campo 'razao_social'...")
collection.create_index([("razao_social", "text")])
print("Índice criado com sucesso.")
