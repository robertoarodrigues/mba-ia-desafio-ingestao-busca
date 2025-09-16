# Desafio MBA Engenharia de Software com IA – Full Cycle


## 📌 Projeto: RAG Chat PDF

Este projeto implementa uma solução de Retrieval-Augmented Generation (RAG) para consulta de documentos em formato PDF, utilizando um banco de dados vetorial e uma interface de chat interativo.
O objetivo é permitir a busca contextualizada em documentos, combinando processamento de linguagem natural com armazenamento vetorial.  

---

## 🚀 Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.10 ou superior  
- Docker e Docker Compose  

---

## ⚙️ Instalação das dependências

Na raiz do projeto, execute os comandos abaixo:

```
python3 -m venv venv
source venv/bin/activate   # Linux / MacOS
venv\Scripts\activate      # Windows PowerShell
pip install -r requirements.txt

```

## 🔧 Configuração do ambiente

Crie um arquivo .env na raiz do projeto com as variáveis de ambiente necessárias.
Exemplo:

```
# Chave da API Gemini
GEMINI_API_KEY=CHANGE_ME

# Configuração do banco de dados
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5434/rag
PG_VECTOR_COLLECTION_NAME=desafio01

# Documento de entrada
PDF_PATH=document.pdf

```
⚠️ Importante: ajuste os valores conforme o seu ambiente.

## ▶️ Execução do projeto

1. Subir o banco de dados vetorial com Docker Compose:

	```
	docker compose up -d
	```

2. Ingestão do PDF no banco vetorial:

	```
	python src/ingest.py
	```

3. Iniciar o chat interativo:

	```
	python src/chat.py
	```

Após iniciar o chat, siga as instruções exibidas no terminal para realizar consultas ao documento.

---

## 📖 Observações

Certifique-se de que o Docker esteja em execução antes de iniciar o banco.

- O arquivo .env deve conter credenciais válidas (ex.: chave da API e configurações do banco).

- Caso deseje utilizar outro documento, altere o valor da variável PDF_PATH.
