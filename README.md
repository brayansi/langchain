# LangChain

Repositório de estudo e referência sobre LangChain, com documentação e exemplos práticos.

## Conteúdo

- **`1-introdução/`** — Documentação:
  - [Introdução ao LangChain](1-introdução/introdução-langchain.md) — visão geral, histórico, recursos e arquitetura básica.
- **`2-fundamentos/`** — Exemplos e documentação:
  - [Fundamentos](2-fundamentos/fundamentos.md) — inicialização de modelos, PromptTemplate e ChatPromptTemplate na prática.

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
pip install langchain langchain-openai langchain-google-genai python-dotenv beautifulsoup4 pypdf
```

### O que é cada pacote?

- **`langchain`**: biblioteca base para construir cadeias, agentes e fluxos com LLMs.
- **`langchain-openai`**: integrações do LangChain com modelos e APIs da OpenAI.
- **`langchain-google-genai`**: integrações do LangChain com modelos Gemini (Google GenAI).
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

Use a seção `1-introdução/` como ponto de partida conceitual e `2-fundamentos/` para praticar os primeiros blocos de construção no código.
