# Gerenciamento e Memorias no LangChain

Esta seção consolida os estudos de gerenciamento de histórico conversacional no LangChain.
O objetivo é mostrar como manter contexto por sessão usando memória em runtime com `RunnableWithMessageHistory`.

Arquivos cobertos nesta seção:

- `1-armazenamoento-de-historico.py`
- `2-historico-sliding-window.py`

---

## 1) Armazenamento de histórico com `RunnableWithMessageHistory`

Arquivo: `5-gerenciamento-e-momeorias/1-armazenamoento-de-historico.py`

Nesse exemplo, você:

1. Carrega variáveis de ambiente com `load_dotenv()`.
2. Inicializa um modelo com `ChatOpenAI`.
3. Cria um prompt de chat com `MessagesPlaceholder(variable_name="history")`.
4. Define um armazenamento por sessão com `InMemoryChatMessageHistory`.
5. Encapsula a chain em `RunnableWithMessageHistory` para persistir o histórico da conversa.
6. Executa múltiplas mensagens reutilizando a mesma `session_id` para manter contexto.

**Casos de uso:**

- Em protótipos de chat com memória de curto prazo.
- Para validar comportamento contextual antes de usar persistência em banco.
- Em estudos sobre fluxo conversacional no padrão moderno de runnables.

---

## 2) Histórico com janela deslizante (sliding window)

Arquivo: `5-gerenciamento-e-momeorias/2-historico-sliding-window.py`

Este exemplo estende o anterior adicionando **truncamento de histórico** com `trim_messages`, reduzindo o número de tokens enviados ao modelo e evitando estouro de contexto.

Conceitos utilizados:

1. **`trim_messages`** — Função que corta o histórico mantendo apenas as mensagens mais recentes dentro de um limite de tokens.
2. **`RunnableLambda`** — Bloco que prepara os inputs antes da chain, aplicando a estratégia de sliding window em `raw_history`.
3. **`history_messages_key="raw_history"`** — O `RunnableWithMessageHistory` injeta o histórico completo em `raw_history`; o `prepare_inputs` corta e repassa em `history`.
4. **Estratégia `"last"`** — Mantém as últimas mensagens; `start_on="human"` garante início em mensagem do usuário; `include_system=True` preserva o system prompt.

**Quando usar:**

- Conversas longas em que o histórico completo excederia o limite de tokens.
- Para reduzir custo e latência em chats iterativos.

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
# preencher OPENAI_API_KEY e/ou GOOGLE_API_KEY

# 4) executar exemplos
python 5-gerenciamento-e-momeorias/1-armazenamoento-de-historico.py
python 5-gerenciamento-e-momeorias/2-historico-sliding-window.py
```
