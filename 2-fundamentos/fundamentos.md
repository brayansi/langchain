# Fundamentos no LangChain

Esta seção consolida os fundamentos práticos para trabalhar com LangChain no projeto.  
O objetivo é mostrar, com exemplos pequenos, como inicializar modelos, estruturar prompts e montar mensagens para chat.

Arquivos cobertos nesta seção:

- `1-hello-world.py`
- `2-init-chat-model.py`
- `3-prompt-template.py`
- `4-chat-prompt-template.py`

## 1) Hello world com `ChatOpenAI`

Arquivo: `2-fundamentos/1-hello-world.py`

Nesse exemplo, você:

1. Carrega variáveis de ambiente com `load_dotenv()`.
2. Inicializa um modelo de chat da OpenAI com `ChatOpenAI`.
3. Envia um prompt simples com `model.invoke(...)`.
4. Imprime o texto final com `message.content`.

Conceitos-chave:

- **`ChatOpenAI`**: cliente para conversar com modelos da OpenAI via interface padronizada do LangChain.
- **`invoke`**: chamada síncrona de inferência.
- **`message.content`**: texto retornado pelo modelo.

Quando usar:

- Teste inicial do ambiente.
- Validação de credenciais (`OPENAI_API_KEY`) e conectividade.
- Primeiro contato com o ciclo mínimo "prompt -> resposta".

## 2) Inicialização agnóstica com `init_chat_model`

Arquivo: `2-fundamentos/2-init-chat-model.py`

Nesse exemplo, você usa:

- `init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")`

Isso mostra o padrão de inicialização por provedor, sem acoplamento direto a uma classe específica de integração.

Conceitos-chave:

- **Portabilidade entre provedores**: mesma ideia de uso, trocando `model` e `model_provider`.
- **Interface uniforme**: depois de inicializar, a chamada continua com `invoke(...)`.

Quando usar:

- Projetos que podem alternar entre OpenAI, Google e outros provedores.
- Cenários onde você quer reduzir lock-in no código de aplicação.

## 3) Prompt parametrizado com `PromptTemplate`

Arquivo: `2-fundamentos/3-prompt-template.py`

Esse arquivo demonstra prompt de texto (não chat) com variáveis:

- Template: `"Hello, {name}!"`
- Variável declarada: `input_variables=["name"]`
- Renderização: `template.format(name="Brayan Santos")`

Conceitos-chave:

- **Separação de template e dados**: evita concatenação manual de strings.
- **Reuso**: o mesmo prompt serve para entradas diferentes.
- **Legibilidade**: facilita manutenção e evolução do prompt.

Quando usar:

- Comandos de uma única mensagem.
- Geração de prompts dinâmicos em pipelines simples.

## 4) Prompt de chat com `ChatPromptTemplate`

Arquivo: `2-fundamentos/4-chat-prompt-template.py`

Esse exemplo mostra como estruturar uma conversa com papéis diferentes:

1. Define mensagens com `ChatPromptTemplate.from_messages(...)`.
2. Usa placeholders para `language` e `question`.
3. Renderiza com `format_messages(...)`.
4. Envia a lista de mensagens para o modelo com `model.invoke(message)`.

Conceitos-chave:

- **Mensagens por papel (`system`, `user`)**: cada mensagem orienta comportamento e contexto.
- **Prompt dinâmico para chat**: variáveis são aplicadas em mensagens estruturadas.
- **Compatibilidade com modelos de chat**: fluxo natural para assistentes conversacionais.

Observação:

- O texto de sistema no exemplo atual indica tradução para uma língua. Isso é útil para estudar instrução de comportamento por papel.

## Como executar os exemplos

No diretório raiz do projeto:

```bash
# 1) ativar ambiente virtual (caso já exista)
source .venv/bin/activate

# 2) instalar dependências
pip install -r requirements.txt

# 3) configurar variáveis de ambiente
cp .env.example .env
# preencher OPENAI_API_KEY e/ou GOOGLE_API_KEY

# 4) executar um exemplo
python 2-fundamentos/1-hello-world.py
```

## Erros comuns e diagnóstico rápido

- **Erro de autenticação**: verifique se a chave API correta está no `.env`.
- **Modelo não encontrado**: confirme nome do modelo e provedor.
- **ImportError**: garanta que as dependências de `requirements.txt` foram instaladas.
- **Resposta vazia ou inesperada**: revise prompt, temperatura e variáveis do template.

## Próximos passos sugeridos

Depois desses fundamentos, você pode evoluir para:

- encadeamento com LCEL (`prompt | model | parser`);
- saída estruturada com schemas;
- uso de tools e agentes;
- RAG com recuperação de contexto externo.
