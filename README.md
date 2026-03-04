# LangChain

Repositório de estudo e referência sobre LangChain, com documentação e exemplos práticos.

## Conteúdo

- **`1-introducao/`** — Documentação:
  - [Introdução ao LangChain](1-introducao/introducao-langchain.md) — visão geral, histórico, recursos e arquitetura básica.
- **`2-fundamentos/`** — Exemplos e documentação:
  - [Fundamentos](2-fundamentos/fundamentos.md) — inicialização de modelos, PromptTemplate e ChatPromptTemplate na prática.
  - Exemplos `.py` da seção:
    - [`1-hello-world.py`](2-fundamentos/1-hello-world.py)
    - [`2-init-chat-model.py`](2-fundamentos/2-init-chat-model.py)
    - [`3-prompt-template.py`](2-fundamentos/3-prompt-template.py)
    - [`4-chat-prompt-template.py`](2-fundamentos/4-chat-prompt-template.py)
- **`3-chains-e-processamento/`** — Exemplos e documentação:
  - [Chains e Processamento](3-chains-e-processamento/chains-e-processamento.md) — composição com LCEL, uso de `@chain`, `RunnableLambda`, pipelines em múltiplas etapas e exemplos de sumarização com `stuff`, `map_reduce` e LCEL.
  - Exemplos `.py` da seção:
    - [`1-init-chains.py`](3-chains-e-processamento/1-init-chains.py)
    - [`2-chains-com-decorators.py`](3-chains-e-processamento/2-chains-com-decorators.py)
    - [`3-runneble-lambda.py`](3-chains-e-processamento/3-runneble-lambda.py)
    - [`4-pipeline-de-processamento.py`](3-chains-e-processamento/4-pipeline-de-processamento.py)
    - [`5-sumarizacao.py`](3-chains-e-processamento/5-sumarizacao.py)
    - [`6-sumarizacao-com-map-reduce.py`](3-chains-e-processamento/6-sumarizacao-com-map-reduce.py)
    - [`7-pipeline-de-sumarizacao.py`](3-chains-e-processamento/7-pipeline-de-sumarizacao.py)
- **`4-agentes-e-tools/`** — Exemplos e documentação:
  - [Agentes e Tools](4-agentes-e-tools/agentes-e-tools.md) — criação de agente no padrão ReAct, definição de tools com `@tool`, uso de prompt customizado e integração com LangChain Hub.
  - Exemplos `.py` da seção:
    - [`1-agente-react-e-tools.py`](4-agentes-e-tools/1-agente-react-e-tools.py)
    - [`2-agente-react-usando-prompt-hub.py`](4-agentes-e-tools/2-agente-react-usando-prompt-hub.py)
- **`5-gerenciamento-e-momeorias/`** — Exemplos e documentação:
  - [Gerenciamento e Memorias](5-gerenciamento-e-momeorias/gerenciamento-e-momeorias.md) — uso de `RunnableWithMessageHistory`, `MessagesPlaceholder` e `InMemoryChatMessageHistory` para manter contexto por `session_id`; histórico com janela deslizante via `trim_messages`.
  - Exemplos `.py` da seção:
    - [`1-armazenamoento-de-historico.py`](5-gerenciamento-e-momeorias/1-armazenamoento-de-historico.py)
    - [`2-historico-sliding-window.py`](5-gerenciamento-e-momeorias/2-historico-sliding-window.py)
- **`6-loading-e-banco-de-dados-vetoriais/`** — Exemplos e documentação:
  - [Loading e Banco de Dados Vetoriais](6-loading-e-banco-de-dados-vetoriais/loading-e-banco-de-dados-vetoriais.md) — carregamento de documentos (WebBaseLoader, PyPDFLoader), segmentação com RecursiveCharacterTextSplitter, ingestão em PGVector e busca vetorial por similaridade.
  - Exemplos `.py` da seção:
    - [`1-carregamento-com-webBaseLoader.py`](6-loading-e-banco-de-dados-vetoriais/1-carregamento-com-webBaseLoader.py)
    - [`2-carregamento-de-pdf.py`](6-loading-e-banco-de-dados-vetoriais/2-carregamento-de-pdf.py)
    - [`3-ingestion-pgvector.py`](6-loading-e-banco-de-dados-vetoriais/3-ingestion-pgvector.py)
    - [`4-search-vector.py`](6-loading-e-banco-de-dados-vetoriais/4-search-vector.py)

## Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/) instalado.
- [pip](https://pip.pypa.io/en/stable/installation/) disponível no ambiente.

## Configuração de ambiente

Crie o arquivo `.env` a partir do exemplo:

```bash
cp .env.example .env
```

Depois, preencha as chaves no `.env`:

- `OPENAI_API_KEY`
- `GOOGLE_API_KEY`
- `PGVECTOR_URL` e `PGVECTOR_COLLECTION` (para exemplos com banco vetorial, seção 6)

## Exemplo rápido

```bash
# Criar e ativar ambiente virtual
python -m venv .venv
source .venv/bin/activate

# Instalar pacotes principais para estudos com LLMs
pip install -r requirements.txt
```

Ou, para instalação manual dos principais pacotes:

```bash
pip install langchain langchain-core langchain-community langchain-openai langchain-google-genai langchain-text-splitters python-dotenv beautifulsoup4 pypdf
```

### Principais pacotes utilizados

| Pacote | Descrição |
|--------|-----------|
| **`langchain`** | Biblioteca base para construir cadeias, agentes e fluxos com LLMs. |
| **`langchain-core`** | Componentes essenciais: `PromptTemplate`, `ChatPromptTemplate`, `RunnableLambda`, `StrOutputParser`, `trim_messages`, etc. |
| **`langchain-community`** | Integrações com fontes externas: `WebBaseLoader`, loaders de documentos e ferramentas de terceiros. |
| **`langchain-openai`** | Integrações com modelos e APIs da OpenAI (GPT). |
| **`langchain-google-genai`** | Integrações com modelos Gemini (Google GenAI). |
| **`langchain-text-splitters`** | Segmentação de texto para pipelines de processamento e sumarização (ex.: `RecursiveCharacterTextSplitter`). |
| **`python-dotenv`** | Carrega variáveis de ambiente de um arquivo `.env` (chaves de API). |
| **`beautifulsoup4`** | Parser de HTML/XML para extração e limpeza de conteúdo web. |
| **`pypdf`** | Leitura e extração de texto de arquivos PDF. |
| **`langchain-postgres`** | Integração com PostgreSQL e pgvector para armazenamento e busca vetorial. |
| **`pgvector`** | Extensão de vetores para PostgreSQL. |

### Salvar dependências do ambiente

Depois de instalar os pacotes, gere o arquivo de dependências do projeto:

```bash
pip freeze > requirements.txt
```

Esse comando lista os pacotes instalados no ambiente virtual atual e salva no arquivo `requirements.txt`. Isso facilita reproduzir o mesmo ambiente em outra máquina com:

```bash
pip install -r requirements.txt
```

Use a seção `1-introducao/` como ponto de partida conceitual, `2-fundamentos/` para praticar os primeiros blocos de construção, `3-chains-e-processamento/` para evoluir na composição de etapas com LCEL, `4-agentes-e-tools/` para orquestrar ferramentas com agentes, `5-gerenciamento-e-momeorias/` para adicionar contexto conversacional com histórico por sessão e `6-loading-e-banco-de-dados-vetoriais/` para carregamento de documentos e busca vetorial com PGVector.
