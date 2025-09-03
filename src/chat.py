import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI,  GoogleGenerativeAIEmbeddings
from langchain_postgres import PGVector
from search import search_prompt

load_dotenv()

def __get_vector_store():
    PG_VECTOR_COLLECTION_NAME = os.getenv("PG_VECTOR_COLLECTION_NAME")
    DATABASE_URL = os.getenv("DATABASE_URL")

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = PGVector(
        embeddings=embeddings,
        collection_name=PG_VECTOR_COLLECTION_NAME,
        connection=DATABASE_URL,
        use_jsonb=True
    )

    return vector_store

def __search_on_vector_store(query):
    vector_store = __get_vector_store()
    results = vector_store.similarity_search_with_score(query, k=10)
    return results

def main(): 
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    chain = search_prompt() | model

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return

    print("Iniciando o chat...")
    print("-" * 60)

    while True:
        if pergunta := input("Faça a sua pergunta: "):
            contexto = __search_on_vector_store(pergunta)
            result = chain.invoke({"contexto": contexto, "pergunta": pergunta})
            
            print("RESPOSTA: ", end="")
            print(result.content)

            print("-" * 10)
            print()
        else:
            print("Encerrando o chat...")
            break

if __name__ == "__main__":
    main()