# Loading e Banco de Dados Vetoriais no LangChain

Esta seção consolida os estudos de carregamento de documentos, segmentação de texto e persistência em banco de dados vetorial (pgvector) com LangChain.
O objetivo é mostrar como usar loaders (WebBase, PDF), text splitters e o PGVector para ingestão e busca semântica.

Arquivos cobertos nesta seção:

- `1-carregamento-com-webBaseLoader.py`
- `2-carregamento-de-pdf.py`
- `3-ingestion-pgvector.py`
- `4-search-vector.py`

---

## 1) Carregamento de páginas web com WebBaseLoader

Arquivo: `6-loading-e-banco-de-dados-vetoriais/1-carregamento-com-webBaseLoader.py`

Nesse exemplo, você:

1. Usa `WebBaseLoader` para carregar conteúdo de páginas web (ex.: langchain.com).
2. Aplica `RecursiveCharacterTextSplitter` para segmentar o documento em chunks de 1000 caracteres com overlap de 200.
3. Itera sobre os chunks gerados para visualização.

**Casos de uso:**

- Carregar documentação ou artigos de sites para RAG.
- Extrair conteúdo de páginas públicas para análise ou indexação.

---

## 2) Carregamento de PDF com PyPDFLoader

Arquivo: `6-loading-e-banco-de-dados-vetoriais/2-carregamento-de-pdf.py`

Este exemplo demonstra o carregamento de arquivos PDF locais:

1. Usa `PyPDFLoader` para carregar um PDF a partir do caminho local.
2. Aplica `RecursiveCharacterTextSplitter` com `chunk_size=500` e `chunk_overlap=100`.
3. Exibe a quantidade de chunks gerados.

**Quando usar:**

- Documentos técnicos, manuais ou PDFs de estudo.
- Pipeline de ingestão de documentos para RAG.

---

## 3) Ingestão em PGVector

Arquivo: `6-loading-e-banco-de-dados-vetoriais/3-ingestion-pgvector.py`

Este exemplo realiza a ingestão de documentos no banco de dados vetorial:

1. Carrega variáveis de ambiente com `load_dotenv()`.
2. Valida `OPENAI_API_KEY`, `PGVECTOR_URL` e `PGVECTOR_COLLECTION`.
3. Carrega o PDF com `PyPDFLoader` e segmenta com `RecursiveCharacterTextSplitter`.
4. Enriquece os documentos removendo metadados vazios.
5. Usa `OpenAIEmbeddings` (text-embedding-3-small) para gerar embeddings.
6. Persiste os documentos no PGVector com IDs definidos.

**Pré-requisitos:**

- PostgreSQL com extensão pgvector rodando (ex.: via `docker-compose up -d`).
- Variáveis `.env` configuradas: `PGVECTOR_URL`, `PGVECTOR_COLLECTION`.

**Exemplo de PGVECTOR_URL:**

```
postgresql://postgres:postgres@localhost:5432/rag
```

---

## 4) Busca vetorial (similarity search)

Arquivo: `6-loading-e-banco-de-dados-vetoriais/4-search-vector.py`

Este exemplo realiza busca por similaridade no banco vetorial:

1. Carrega variáveis de ambiente e valida as mesmas do exemplo anterior.
2. Conecta ao PGVector com `OpenAIEmbeddings`.
3. Executa `similarity_search_with_score` com uma query e `k=3` resultados.
4. Exibe o conteúdo e metadados de cada resultado com seu score.

**Quando usar:**

- RAG: recuperar documentos relevantes antes de enviar ao LLM.
- Busca semântica em bases de conhecimento indexadas.

---

## Infraestrutura: PostgreSQL + pgvector

O projeto inclui um `docker-compose.yaml` para subir PostgreSQL com a extensão pgvector:

```bash
docker-compose up -d
```

O serviço `bootstrap_vector_ext` cria a extensão `vector` automaticamente após o banco estar saudável.

---

## Como executar os exemplos

No diretório raiz do projeto:

```bash
# 1) ativar ambiente virtual
source .venv/bin/activate

# 2) instalar dependências
pip install -r requirements.txt

# 3) configurar variáveis de ambiente
cp .env.example .env
# preencher OPENAI_API_KEY, PGVECTOR_URL, PGVECTOR_COLLECTION
# ex.: PGVECTOR_URL=postgresql://postgres:postgres@localhost:5432/rag

# 4) subir PostgreSQL + pgvector (para exemplos 3 e 4)
docker-compose up -d

# 5) executar exemplos
python 6-loading-e-banco-de-dados-vetoriais/1-carregamento-com-webBaseLoader.py
python 6-loading-e-banco-de-dados-vetoriais/2-carregamento-de-pdf.py
python 6-loading-e-banco-de-dados-vetoriais/3-ingestion-pgvector.py
python 6-loading-e-banco-de-dados-vetoriais/4-search-vector.py
```
