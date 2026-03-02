# Gerenciamento e Memorias no LangChain

Esta seção consolida os estudos de gerenciamento de histórico conversacional no LangChain.
O objetivo é mostrar como manter contexto por sessão usando memória em runtime com `RunnableWithMessageHistory`.

Arquivos cobertos nesta seção:

- `1-armazenamoento-de-historico.py`

## 1) Armazenamento de histórico com `RunnableWithMessageHistory`

Arquivo: `5-gerenciamento-e-momeorias/1-armazenamoento-de-historico.py`

Nesse exemplo, você:

1. Carrega variáveis de ambiente com `load_dotenv()`.
2. Inicializa um modelo com `ChatOpenAI`.
3. Cria um prompt de chat com `MessagesPlaceholder(variable_name="history")`.
4. Define um armazenamento por sessão com `InMemoryChatMessageHistory`.
5. Encapsula a chain em `RunnableWithMessageHistory` para persistir o histórico da conversa.
6. Executa múltiplas pErros comuns e diagnóstico rápido
Erro de autenticação: valide as chaves de API no .env.
Histórico não sendo lembrado: confira se a mesma session_id está sendo reaproveitada nas chamadas.
Chaves de entrada inconsistentes: valide input_messages_key="input" e history_messages_key="history" no RunnableWithMessageHistory.
ImportError: confirme instalação das dependências com pip install -r requirements.txt.
Memória perdida entre execuções: comportamento esperado de InMemoryChatMessageHistory (não persiste após encerrar o processo).
Próximos passos sugeridos
Depois desta seção, você pode evoluir para:

memória persistida em banco ou cache externo;
estratégia de resumo de histórico para reduzir tokens;
múltiplas sessões concorrentes por usuário;
combinação de memória conversacional com RAG.

- Em protótipos de chat com memória de curto prazo.
- Para validar comportamento contextual antes de usar persistência em banco.
- Em estudos sobre fluxo conversacional no padrão moderno de runnables.

## Como executar o exemplo

No diretório raiz do projeto:

```bash
# 1) ativar ambiente virtual
source .venv/bin/activate

# 2) instalar dependências
pip install -r requirements.txt

# 3) configurar variáveis de ambiente
cp .env.example .env
# preencher OPENAI_API_KEY e/ou GOOGLE_API_KEY

# 4) executar exemplo
python 5-gerenciamento-e-momeorias/1-armazenamoento-de-historico.py
```