

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
from datetime import datetime

MONGO_URI = "mongodb+srv://cardoneluisfelipe08:cardoneregim@cluster0.rzcpwpu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DB_NAME = "ecossistema_uberlandia"

try:
    client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
    db = client[DB_NAME]

    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    print(f"Conectado ao banco de dados '{DB_NAME}' com sucesso!")

    segmentos_data = [
        {
            "_id": "tecnologia",
            "nome": "Tecnologia da Informação",
            "descricao": "Empresas de software, hardware, TI e serviços digitais.",
            "palavras_chave": ["software", "hardware", "desenvolvimento", "cybersegurança", "cloud"]
        },
        {
            "_id": "marketing",
            "nome": "Marketing e Publicidade",
            "descricao": "Agências de marketing digital, branding, publicidade e comunicação.",
            "palavras_chave": ["digital", "branding", "publicidade", "seo", "midiassociais"]
        },
        {
            "_id": "logistica",
            "nome": "Logística e Transporte",
            "descricao": "Empresas de transporte, armazenagem, distribuição e cadeia de suprimentos.",
            "palavras_chave": ["transporte", "armazenagem", "distribuição", "frota", "frete"]
        },
        {
            "_id": "agro",
            "nome": "Agronegócio",
            "descricao": "Empresas ligadas à agricultura, pecuária e insumos agrícolas.",
            "palavras_chave": ["agricultura", "pecuaria", "insumos", "fazenda", "colheita"]
        },
        {
            "_id": "saude",
            "nome": "Saúde e Bem-estar",
            "descricao": "Clínicas, hospitais, farmácias e serviços de saúde.",
            "palavras_chave": ["hospital", "clinica", "farmacia", "medicina", "bemestar"]
        }
    ]
    if db.segmentos.count_documents({}) == 0:
        db.segmentos.insert_many(segmentos_data)
        print("Documentos inseridos na coleção 'segmentos'.")
    else:
        print("Coleção 'segmentos' já contém documentos. Pulando inserção.")

    empresas_data = [
        {
            "nome_fantasia": "Tech Solutions Udi",
            "razao_social": "Tecnologia Soluções LTDA",
            "cnpj": "11.222.333/0001-44",
            "endereco": {
                "rua": "Av. Rondon Pacheco",
                "numero": "1234",
                "bairro": "Santa Mônica",
                "cidade": "Uberlândia",
                "estado": "MG",
                "cep": "38400-000"
            },
            "contato": {
                "email": "contato@techsolutions.com",
                "telefone": "(34) 99876-5432",
                "site": "www.techsolutions.com"
            },
            "segmentos": ["tecnologia", "consultoria"],
            "tempo_atuacao_anos": 10,
            "porte": "Grande",
            "servicos_produtos": [
                "Desenvolvimento de Software Customizado",
                "Consultoria em TI",
                "Cybersegurança",
                "Sistemas ERP"
            ],
            "objetivos_networking": [
                "Parceiros de Hardware",
                "Clientes de Grande Porte",
                "Investidores"
            ],
            "data_cadastro": datetime(2015, 3, 20, 10, 0, 0),
            "ultima_atualizacao": datetime.now()
        },
        {
            "nome_fantasia": "Mídia Genial",
            "razao_social": "Mídia Genial Comunicação S.A.",
            "cnpj": "22.333.444/0001-55",
            "endereco": {
                "rua": "Av. João Naves de Ávila",
                "numero": "567",
                "bairro": "Tibery",
                "cidade": "Uberlândia",
                "estado": "MG",
                "cep": "38400-100"
            },
            "contato": {
                "email": "contato@midiagenial.com.br",
                "telefone": "(34) 99123-4567",
                "site": "www.midiagenial.com.br"
            },
            "segmentos": ["marketing", "design"],
            "tempo_atuacao_anos": 5,
            "porte": "Média",
            "servicos_produtos": [
                "Marketing Digital",
                "Gestão de Redes Sociais",
                "Criação de Campanhas",
                "Design Gráfico"
            ],
            "objetivos_networking": [
                "Desenvolvedores Web",
                "Produtoras de Vídeo",
                "Clientes para branding"
            ],
            "data_cadastro": datetime(2020, 7, 15, 9, 30, 0),
            "ultima_atualizacao": datetime.now()
        },
        {
            "nome_fantasia": "LogiRápida Uberlândia",
            "razao_social": "Logística Rápida UDI LTDA",
            "cnpj": "33.444.555/0001-66",
            "endereco": {
                "rua": "Rua do Caminhoneiro",
                "numero": "789",
                "bairro": "Distrito Industrial",
                "cidade": "Uberlândia",
                "estado": "MG",
                "cep": "38405-000"
            },
            "contato": {
                "email": "contato@logirapida.com",
                "telefone": "(34) 98765-4321",
                "site": "www.logirapida.com"
            },
            "segmentos": ["logistica"],
            "tempo_atuacao_anos": 12,
            "porte": "Grande",
            "servicos_produtos": [
                "Transporte de Cargas",
                "Armazenagem",
                "Distribuição",
                "Gestão de Estoque"
            ],
            "objetivos_networking": [
                "Empresas de E-commerce",
                "Fornecedores de Embalagens",
                "Parceiros de Software de Gestão"
            ],
            "data_cadastro": datetime(2013, 11, 1, 14, 15, 0),
            "ultima_atualizacao": datetime.now()
        },
        {
            "nome_fantasia": "AgroFuturo MG",
            "razao_social": "Agro Futuro Uberlândia S.A.",
            "cnpj": "44.555.666/0001-77",
            "endereco": {
                "rua": "Estrada da Água Limpa",
                "numero": "999",
                "bairro": "Zona Rural",
                "cidade": "Uberlândia",
                "estado": "MG",
                "cep": "38400-000"
            },
            "contato": {
                "email": "contato@agrofuturo.com.br",
                "telefone": "(34) 99234-5678",
                "site": "www.agrofuturo.com.br"
            },
            "segmentos": ["agro"],
            "tempo_atuacao_anos": 8,
            "porte": "Média",
            "servicos_produtos": [
                "Consultoria Agrícola",
                "Venda de Insumos",
                "Máquinas Agrícolas",
                "Monitoramento de Lavoura"
            ],
            "objetivos_networking": [
                "Cooperativas",
                "Empresas de Tecnologia para o Campo",
                "Exportadoras"
            ],
            "data_cadastro": datetime(2017, 6, 25, 11, 0, 0),
            "ultima_atualizacao": datetime.now()
        },
        {
            "nome_fantasia": "Clínica Vida Ativa",
            "razao_social": "Clínica Médica Vida Ativa LTDA",
            "cnpj": "55.666.777/0001-88",
            "endereco": {
                "rua": "Av. Getúlio Vargas",
                "numero": "321",
                "bairro": "Centro",
                "cidade": "Uberlândia",
                "estado": "MG",
                "cep": "38400-000"
            },
            "contato": {
                "email": "contato@vidativa.com",
                "telefone": "(34) 99345-6789",
                "site": "www.vidativa.com"
            },
            "segmentos": ["saude"],
            "tempo_atuacao_anos": 15,
            "porte": "Pequena",
            "servicos_produtos": [
                "Consultas Médicas",
                "Exames Laboratoriais",
                "Fisioterapia",
                "Nutrição"
            ],
            "objetivos_networking": [
                "Laboratórios de Análises",
                "Fornecedores de Equipamentos Médicos",
                "Planos de Saúde"
            ],
            "data_cadastro": datetime(2010, 1, 5, 8, 0, 0),
            "ultima_atualizacao": datetime.now()
        }
    ]
    if db.empresas.count_documents({}) == 0:
        db.empresas.insert_many(empresas_data)
        print("Documentos inseridos na coleção 'empresas'.")
    else:
        print("Coleção 'empresas' já contém documentos. Pulando inserção.")

    tech_solutions_udi_obj = db.empresas.find_one({"nome_fantasia": "Tech Solutions Udi"})
    midia_genial_obj = db.empresas.find_one({"nome_fantasia": "Mídia Genial"})
    logirapida_uberlandia_obj = db.empresas.find_one({"nome_fantasia": "LogiRápida Uberlândia"})
    agrofuturo_mg_obj = db.empresas.find_one({"nome_fantasia": "AgroFuturo MG"})
    clinica_vida_ativa_obj = db.empresas.find_one({"nome_fantasia": "Clínica Vida Ativa"})

    if not all([tech_solutions_udi_obj, midia_genial_obj, logirapida_uberlandia_obj, agrofuturo_mg_obj, clinica_vida_ativa_obj]):
        print("Erro: Não foi possível encontrar todas as empresas para criar as parcerias. Certifique-se de que a coleção 'empresas' foi preenchida.")
    else:
        parcerias_data = [
            {
                "empresa_origem_id": tech_solutions_udi_obj["_id"],
                "empresa_destino_id": midia_genial_obj["_id"],
                "tipo_parceria": "Desenvolvimento Conjunto",
                "descricao": "Criação de uma plataforma de marketing digital unificada.",
                "data_inicio": datetime(2023, 1, 10),
                "status": "Ativa",
                "contatos_envolvidos": [
                    {"empresa_id": tech_solutions_udi_obj["_id"], "nome_contato": "João Silva", "cargo": "CTO"},
                    {"empresa_id": midia_genial_obj["_id"], "nome_contato": "Maria Oliveira", "cargo": "Diretora de Marketing"}
                ],
                "relevancia": 5
            },
            {
                "empresa_origem_id": logirapida_uberlandia_obj["_id"],
                "empresa_destino_id": agrofuturo_mg_obj["_id"],
                "tipo_parceria": "Logística",
                "descricao": "Transporte e armazenagem de insumos agrícolas.",
                "data_inicio": datetime(2022, 5, 1),
                "status": "Ativa",
                "contatos_envolvidos": [
                    {"empresa_id": logirapida_uberlandia_obj["_id"], "nome_contato": "Carlos Santos", "cargo": "Gerente de Operações"},
                    {"empresa_id": agrofuturo_mg_obj["_id"], "nome_contato": "Ana Costa", "cargo": "Gerente de Produção"}
                ],
                "relevancia": 4
            },
            {
                "empresa_origem_id": clinica_vida_ativa_obj["_id"],
                "empresa_destino_id": tech_solutions_udi_obj["_id"],
                "tipo_parceria": "Tecnologia",
                "descricao": "Desenvolvimento de um sistema de agendamento online para a clínica.",
                "data_inicio": datetime(2024, 3, 1),
                "status": "Em Negociação",
                "contatos_envolvidos": [
                    {"empresa_id": clinica_vida_ativa_obj["_id"], "nome_contato": "Dr. Fernando Lima", "cargo": "Diretor Clínico"},
                    {"empresa_id": tech_solutions_udi_obj["_id"], "nome_contato": "Beatriz Nogueira", "cargo": "Gerente de Projetos"}
                ],
                "relevancia": 3
            }
        ]
        if db.parcerias.count_documents({}) == 0:
            db.parcerias.insert_many(parcerias_data)
            print("Documentos inseridos na coleção 'parcerias'.")
        else:
            print("Coleção 'parcerias' já contém documentos. Pulando inserção.")

    print("\n--- Documentos na coleção 'segmentos': ---")
    for doc in db.segmentos.find():
        print(doc)

    print("\n--- Documentos na coleção 'empresas': ---")
    for doc in db.empresas.find():
        print(doc)

    print("\n--- Documentos na coleção 'parcerias': ---")
    for doc in db.parcerias.find():
        print(doc)

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    if 'client' in locals() and client:
        client.close()
        print("\nConexão com o MongoDB fechada.")
