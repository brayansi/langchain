# Fundamentos no LangChain

Esta secao consolida os fundamentos praticos para trabalhar com LangChain no projeto.  
O objetivo e mostrar, com exemplos pequenos, como inicializar modelos, estruturar prompts e montar mensagens para chat.

Arquivos cobertos nesta secao:

- `1-hello-world.py`
- `2-init-chat-model.py`
- `3-prompt-template.py`
- `4-chat-prompt-template.py`

## 1) Hello world com `ChatOpenAI`

Arquivo: `2-fundamentos/1-hello-world.py`

Nesse exemplo, voce:

1. Carrega variaveis de ambiente com `load_dotenv()`.
2. Inicializa um modelo de chat da OpenAI com `ChatOpenAI`.
3. Envia um prompt simples com `model.invoke(...)`.
4. Imprime o texto final com `message.content`.

Conceitos-chave:

- **`ChatOpenAI`**: cliente para conversar com modelos da OpenAI via interface padronizada do LangChain.
- **`invoke`**: chamada sincrona de inferencia.
- **`message.content`**: texto retornado pelo modelo.

Quando usar:

- Teste inicial do ambiente.
- Validacao de credenciais (`OPENAI_API_KEY`) e conectividade.
- Primeiro contato com o ciclo minimo "prompt -> resposta".

## 2) Inicializacao agnostica com `init_chat_model`

Arquivo: `2-fundamentos/2-init-chat-model.py`

Nesse exemplo, voce usa:

- `init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")`

Isso mostra o padrao de inicializacao por provedor, sem acoplamento direto a uma classe especifica de integracao.

Conceitos-chave:

- **Portabilidade entre provedores**: mesma ideia de uso, trocando `model` e `model_provider`.
- **Interface uniforme**: depois de inicializar, a chamada continua com `invoke(...)`.

Quando usar:

- Projetos que podem alternar entre OpenAI, Google e outros provedores.
- Cenarios onde voce quer reduzir lock-in no codigo de aplicacao.

## 3) Prompt parametrizado com `PromptTemplate`

Arquivo: `2-fundamentos/3-prompt-template.py`

Esse arquivo demonstra prompt de texto (nao chat) com variaveis:

- Template: `"Hello, {name}!"`
- Variavel declarada: `input_variables=["name"]`
- Renderizacao: `template.format(name="Brayan Santos")`

Conceitos-chave:

- **Separacao de template e dados**: evita concatenacao manual de strings.
- **Reuso**: o mesmo prompt serve para entradas diferentes.
- **Legibilidade**: facilita manutencao e evolucao do prompt.

Quando usar:

- Comandos de uma unica mensagem.
- Geracao de prompts dinamicos em pipelines simples.

## 4) Prompt de chat com `ChatPromptTemplate`

Arquivo: `2-fundamentos/4-chat-prompt-template.py`

Esse exemplo mostra como estruturar uma conversa com papeis diferentes:

1. Define mensagens com `ChatPromptTemplate.from_messages(...)`.
2. Usa placeholders para `language` e `question`.
3. Renderiza com `format_messages(...)`.
4. Envia a lista de mensagens para o modelo com `model.invoke(message)`.

Conceitos-chave:

- **Mensagens por papel (`system`, `user`)**: cada mensagem orienta comportamento e contexto.
- **Prompt dinamico para chat**: variaveis sao aplicadas em mensagens estruturadas.
- **Compatibilidade com modelos de chat**: fluxo natural para assistentes conversacionais.

Observacao:

- O texto de sistema no exemplo atual indica traducao para uma lingua. Isso e util para estudar instrucao de comportamento por papel.

## Como executar os exemplos

No diretorio raiz do projeto:

```bash
# 1) ativar ambiente virtual (caso ja exista)
source .venv/bin/activate

# 2) instalar dependencias
pip install -r requirements.txt

# 3) configurar variaveis de ambiente
cp .env.example .env
# preencher OPENAI_API_KEY e/ou GOOGLE_API_KEY

# 4) executar um exemplo
python 2-fundamentos/1-hello-world.py
```

## Erros comuns e diagnostico rapido

- **Erro de autenticacao**: verifique se a chave API correta esta no `.env`.
- **Modelo nao encontrado**: confirme nome do modelo e provedor.
- **ImportError**: garanta que as dependencias de `requirements.txt` foram instaladas.
- **Resposta vazia ou inesperada**: revise prompt, temperatura e variaveis do template.

## Proximos passos sugeridos

Depois desses fundamentos, voce pode evoluir para:

- encadeamento com LCEL (`prompt | model | parser`);
- saida estruturada com schemas;
- uso de tools e agentes;
- RAG com recuperacao de contexto externo.
