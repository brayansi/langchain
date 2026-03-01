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
  - [Agentes e Tools](4-agentes-e-tools/agentes-e-tools.md) — criação de agente no padrão ReAct, definição de tools com `@tool` e execução controlada com `AgentExecutor`.
  - Exemplos `.py` da seção:
    - [`1-agente-react-e-tools.py`](4-agentes-e-tools/1-agente-react-e-tools.py)

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

## Exemplo rápido

```bash
# Criar e ativar ambiente virtual
python -m venv .venv
source .venv/bin/activate

# Instalar pacotes principais para estudos com LLMs
pip install langchain langchain-openai langchain-google-genai langchain-text-splitters python-dotenv beautifulsoup4 pypdf
```

### O que é cada pacote?

- **`langchain`**: biblioteca base para construir cadeias, agentes e fluxos com LLMs.
- **`langchain-openai`**: integrações do LangChain com modelos e APIs da OpenAI.
- **`langchain-google-genai`**: integrações do LangChain com modelos Gemini (Google GenAI).
- **`langchain-text-splitters`**: utilitários de segmentação de texto para pipelines de processamento e sumarização.
- **`python-dotenv`**: carrega variáveis de ambiente de um arquivo `.env` (ex.: chaves de API).
- **`beautifulsoup4`**: parser de HTML/XML para extração e limpeza de conteúdo web.
- **`pypdf`**: leitura e extração de texto de arquivos PDF.

### Salvar dependências do ambiente

Depois de instalar os pacotes, gere o arquivo de dependências do projeto:

```bash
pip freeze > requirements.txt
```

Esse comando lista os pacotes instalados no ambiente virtual atual e salva no arquivo `requirements.txt`. Isso facilita reproduzir o mesmo ambiente em outra máquina com:

```bash
pip install -r requirements.txt
```

Use a seção `1-introducao/` como ponto de partida conceitual, `2-fundamentos/` para praticar os primeiros blocos de construção, `3-chains-e-processamento/` para evoluir na composição de etapas com LCEL e `4-agentes-e-tools/` para orquestrar ferramentas com agentes.
