# Introdução ao LangChain e seu ecossistema

O LangChain é um framework open source para construir aplicações com LLMs de forma modular. Em vez de usar apenas chamadas isoladas de modelo, ele oferece uma arquitetura para combinar modelos, ferramentas, recuperação de contexto (RAG), memória, streaming e observabilidade.

Na prática, você consegue sair de um protótipo simples para um sistema de produção mantendo a mesma linha de desenvolvimento.

## Visão geral do ecossistema (ponta a ponta)

Hoje, o ecossistema pode ser entendido assim:

- **LangChain**: camada de alto nível para criar agentes e apps rapidamente.
- **LangGraph**: camada de orquestração mais baixa para fluxos stateful, long-running e com controle fino.
- **LangSmith**: plataforma para observabilidade, avaliação, testes e operação em produção.
- **LangSmith Deployment (Agent Server)**: runtime de deploy para agentes com execução durável, streaming e escala.
- **LangSmith Studio**: IDE visual para depuração, inspeção de estado, testes e iteração.
- **LangServe**: biblioteca para expor runnables/chains via API REST; segue útil em casos específicos, mas o próprio time recomenda LangGraph Platform para novos projetos.

## Como escolher cada camada

Uma regra simples:

- Comece por **LangChain** quando quiser produtividade e padrões prontos.
- Use **LangGraph** quando precisar de controle de fluxo complexo (loops, interrupções, persistência, HITL).
- Use **LangSmith** desde cedo para rastrear execução, medir qualidade e reduzir risco em produção.

Importante: os agentes do LangChain são construídos sobre LangGraph, então você não "perde" capacidade ao iniciar no alto nível.

## Principais conceitos técnicos no LangChain atual

- **Agents (`create_agent`)**: forma recomendada para construir agentes em produção.
- **Models**: interface padronizada para trocar provedores com menos lock-in.
- **Tools**: funções e integrações que o agente chama durante o raciocínio.
- **Retrieval e RAG**: recuperação de conhecimento externo para respostas ancoradas em dados.
- **Middleware**: ponto de extensão para guardrails, roteamento, políticas e observabilidade.
- **State e Memory**: histórico da conversa e estado adicional para comportamento contextual.
- **Structured output**: saída tipada/estruturada com estratégias de provider ou tool.
- **Streaming**: resposta incremental para melhor UX e monitoramento em tempo real.

## Mudanças importantes na geração mais recente (v1+)

Para estudar sem pegar material antigo, tenha estes pontos em mente:

- O pacote `langchain` ficou mais enxuto e focado em blocos centrais.
- Recursos legados (ex.: `LLMChain`, `ConversationChain`) foram movidos para `langchain-classic`.
- A recomendação atual para agentes é `langchain.agents.create_agent`.
- O ecossistema atual reforça middleware, estado e estratégias de runtime para produção.

## Fluxo ponta a ponta de um projeto

Um caminho típico de ponta a ponta no ecossistema:

1. **Descoberta do caso de uso**: definir tarefa, métricas de sucesso e riscos.
2. **Protótipo local**: montar agente/app com LangChain e ferramentas básicas.
3. **Contexto externo**: adicionar retrieval (RAG), banco vetorial e fontes de dados.
4. **Confiabilidade**: inserir middleware, validações e controles de erro.
5. **Observabilidade**: instrumentar com LangSmith para tracing e avaliação.
6. **Iteração de qualidade**: ajustar prompt, tools, retrieval e critérios de avaliação.
7. **Deploy**: publicar em Agent Server/Deployment com escala e execução durável.
8. **Operação contínua**: monitorar custo, latência, qualidade e regressão.
