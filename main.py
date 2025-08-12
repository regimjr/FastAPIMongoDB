
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId # Importe para converter _id

# Configurações do MongoDB
# Substitua com a sua string de conexão do MongoDB Atlas
MONGO_URI = "mongodb+srv://cardoneluisfelipe08:cardoneregim@cluster0.rzcpwpu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "ecossistema_uberlandia"
COLLECTION_NAME = "empresas"

# Inicializar o FastAPI
app = FastAPI()

# Conectar ao MongoDB
try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Erro ao conectar ao MongoDB: {e}")

# Rota de busca usando o índice
@app.get("/buscar")
async def buscar_empresas(termo: str):
    """
    Busca empresas na coleção 'empresas' usando um índice.
    A busca será feita no campo 'razao_social'.
    """
    if not termo:
        raise HTTPException(status_code=400, detail="O parâmetro 'termo' é obrigatório.")

    # Realiza a busca no MongoDB
    resultados = list(collection.find(
        { "razao_social": { "$regex": termo, "$options": "i" } } # Use $regex para busca parcial case-insensitive
    ))

    if not resultados:
        raise HTTPException(status_code=404, detail="Nenhuma empresa encontrada com o termo fornecido.")

    # Converter _id de ObjectId para string para ser serializado pelo FastAPI
    for resultado in resultados:
        resultado["_id"] = str(resultado["_id"])

    return {"resultados": resultados}

# Operação 1: Contagem de empresas por segmento
@app.get("/estatisticas/segmentos")
async def get_segmentos_stats():
    try:
        pipeline = [
            # Stage 1: Desagrupa o array 'segmentos' para tratar cada segmento individualmente
            {"$unwind": "$segmentos"},
            # Stage 2: Agrupa por nome do segmento e conta os documentos
            {
                "$group": {
                    "_id": "$segmentos.nome_segmento",
                    "total_empresas": {"$count": {}}
                }
            },
            # Stage 3: Ordena os resultados do maior para o menor
            {"$sort": {"total_empresas": -1}}
        ]

        resultados = list(collection.aggregate(pipeline))
        
        return resultados
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Operação 2: Média de tempo de atuação por segmento
@app.get("/estatisticas/tempo_atuacao")
async def get_tempo_atuacao_stats():
    try:
        pipeline = [
            # Stage 1: Desagrupa o array 'segmentos'
            {"$unwind": "$segmentos"},
            # Stage 2: Filtra documentos que têm o campo tempo_atuacao_anos
            {"$match": {"tempo_atuacao_anos": {"$exists": True, "$ne": None}}},
            # Stage 3: Agrupa por nome do segmento e calcula a média
            {
                "$group": {
                    "_id": "$segmentos.nome_segmento",
                    "media_tempo_atuacao": {"$avg": "$tempo_atuacao_anos"}
                }
            },
            # Stage 4: Ordena os resultados pela média
            {"$sort": {"media_tempo_atuacao": -1}}
        ]

        resultados = list(collection.aggregate(pipeline))

        return resultados
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))