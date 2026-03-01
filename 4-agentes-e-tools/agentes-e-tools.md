# Agentes e Tools no LangChain

Esta seção consolida os estudos de agentes com ferramentas no LangChain.
O objetivo é mostrar como um agente ReAct decide quando chamar tools e como compor regras de execução com `AgentExecutor`.

Arquivos cobertos nesta seção:

- `1-agente-react-e-tools.py`

## 1) Agente ReAct com tools customizadas

Arquivo: `4-agentes-e-tools/1-agente-react-e-tools.py`

Esse exemplo monta um agente com duas tools:

1. Cria a tool `calculator` para resolver expressões matemáticas simples.
2. Cria a tool `web_search_mock` para responder capitais com base em um dicionário local.
3. Inicializa o modelo com `ChatOpenAI`.
4. Define um prompt ReAct com formato `Thought -> Action -> Observation -> Final Answer`.
5. Monta o agente com `create_react_agent(...)`.
6. Executa com `AgentExecutor` e `invoke(...)`.

Conceitos-chave:

- **ReAct**: o modelo alterna raciocínio e uso de ferramentas para chegar à resposta.
- **`@tool`**: transforma funções Python em ferramentas invocáveis pelo agente.
- **`AgentExecutor`**: controla execução, número de iterações e tratamento de erro de parsing.
- **Prompt com regras explícitas**: restringe o agente a usar somente informações das tools.

Quando usar:

- Quando o LLM precisa consultar funções externas para responder.
- Para separar capacidades do agente em tools pequenas e reutilizáveis.
- Em fluxos que exigem rastreabilidade das ações (`verbose=True`).

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
python 4-agentes-e-tools/1-agente-react-e-tools.py
```

## Erros comuns e diagnóstico rápido

- **ImportError do `tool`**: confirme `from langchain.tools import tool`.
- **Erro de autenticação**: valide chaves no `.env` e permissões da API.
- **Loop ou resposta incompleta**: ajuste `max_iterations` no `AgentExecutor`.
- **Parsing error no ReAct**: revise o formato do prompt (`Action`, `Action Input`, `Final Answer`).
- **Risco com `eval` na tool de cálculo**: evite entrada não confiável ou substitua por parser matemático seguro.

## Próximos passos sugeridos

Depois desta seção, você pode evoluir para:

- tools com schemas de entrada estruturada;
- agentes com memória e contexto persistente;
- integração com busca real, banco e APIs externas;
- estratégias de fallback e validação de saída do agente.
