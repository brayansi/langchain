# LangChain

Repositório de estudo e referência sobre LangChain, com documentação e exemplos práticos.

## Conteúdo

- **`intro/`** — Documentação:
  - [Introdução ao LangChain](intro/intro-langchain.md) — visão geral, histórico, recursos e arquitetura básica.

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

### O que e cada pacote?

- **`langchain`**: biblioteca base para construir cadeias, agentes e fluxos com LLMs.
- **`langchain-openai`**: integracoes do LangChain com modelos e APIs da OpenAI.
- **`langchain-google-genai`**: integracoes do LangChain com modelos Gemini (Google GenAI).
- **`python-dotenv`**: carrega variaveis de ambiente de um arquivo `.env` (ex.: chaves de API).
- **`beautifulsoup4`**: parser de HTML/XML para extracao e limpeza de conteudo web.
- **`pypdf`**: leitura e extracao de texto de arquivos PDF.

### Salvar dependencias do ambiente

Depois de instalar os pacotes, gere o arquivo de dependencias do projeto:

```bash
pip freeze > requirements.txt
```

Esse comando lista os pacotes instalados no ambiente virtual atual e salva no arquivo `requirements.txt`. Isso facilita reproduzir o mesmo ambiente em outra maquina com:

```bash
pip install -r requirements.txt
```

Use a seção `intro/` como ponto de partida para entender os conceitos fundamentais.
