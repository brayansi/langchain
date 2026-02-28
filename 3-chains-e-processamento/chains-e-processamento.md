# Chains e Processamento no LangChain

Esta secao consolida os estudos de encadeamento e transformacao de dados com LCEL no projeto.
O objetivo e mostrar como combinar etapas com o operador `|`, criar funcoes reutilizaveis e processar entrada/saida com runnables.

Arquivos cobertos nesta secao:

- `1-init-chains.py`
- `2-chains-com-decorators.py`
- `3-runneble-lambda.py`
- `4-pipeline-de-processamento.py`

## 1) Encadeamento basico com `PromptTemplate | model`

Arquivo: `3-chains-e-processamento/1-init-chains.py`

Nesse exemplo, voce:

1. Carrega variaveis de ambiente com `load_dotenv()`.
2. Cria um `PromptTemplate` com variavel dinamica (`topic`).
3. Inicializa o modelo com `ChatOpenAI`.
4. Encadeia `template | model` para formar uma chain simples.
5. Executa com `invoke(...)` e imprime `response.content`.

Conceitos-chave:

- **LCEL (`|`)**: conecta componentes de forma declarativa, onde a saida de uma etapa alimenta a proxima.
- **`invoke`**: executa a cadeia inteira em uma chamada sincrona.
- **Composicao simples**: bom ponto de partida para pipelines pequenos.

Quando usar:

- Geracao de texto a partir de um prompt parametrizado.
- Fluxos de uma unica etapa de transformacao + inferencia.
- Teste rapido de prompts reaproveitaveis.

## 2) Chain customizada com decorator `@chain`

Arquivo: `3-chains-e-processamento/2-chains-com-decorators.py`

Esse exemplo adiciona uma etapa Python antes do prompt:

1. Define uma funcao com `@chain` para processar dados de entrada.
2. A funcao recebe `{ "x": ... }` e retorna `{ "squere_result": ... }`.
3. O resultado alimenta o `PromptTemplate`.
4. O modelo recebe o prompt final e gera a resposta.

Conceitos-chave:

- **`@chain`**: transforma funcao Python em runnable compativel com LCEL.
- **Pre-processamento**: permite calcular/normalizar dados antes da chamada ao LLM.
- **Contrato de dados entre etapas**: chaves de entrada e saida precisam estar alinhadas.

Quando usar:

- Fluxos com regra de negocio antes do LLM.
- Casos em que voce quer separar transformacao de dados e geracao de texto.
- Pipelines com mais controle sobre o formato de entrada.

## 3) Conversao de tipo com `RunnableLambda`

Arquivo: `3-chains-e-processamento/3-runneble-lambda.py`

Esse exemplo mostra uma transformacao isolada:

1. Cria a funcao `parse_number(text: str) -> int`.
2. Encapsula a funcao com `RunnableLambda`.
3. Executa com `invoke("10")`.
4. Retorna `int` em vez de `str`.

Conceitos-chave:

- **`RunnableLambda`**: adapta funcoes Python para o ecossistema de runnables.
- **Transformacao de entrada/saida**: util para preparar dados entre etapas.
- **Reuso composicional**: funcoes pequenas podem ser combinadas em chains maiores.

Quando usar:

- Parsing de dados recebidos como texto.
- Normalizacao e validacao antes de prompts/modelos.
- Composicao de pipelines com etapas tecnicas e sem LLM.

## 4) Pipeline de processamento com traducao + resumo

Arquivo: `3-chains-e-processamento/4-pipeline-de-processamento.py`

Esse exemplo monta um fluxo em duas etapas com parser de saida:

1. Cria um prompt para traducao (`initial_text -> text em ingles`).
2. Encadeia o modelo com `StrOutputParser()` para garantir retorno em `str`.
3. Usa a saida da traducao como entrada de um segundo prompt de resumo.
4. Gera a resposta final com outro `StrOutputParser()`.

Conceitos-chave:

- **Pipeline com multiplas etapas**: combina transformacao intermediaria e resultado final.
- **Mapeamento de entrada com dict runnable**: `{ "text": translate }` conecta a saida de uma subchain a outra etapa.
- **`StrOutputParser`**: remove dependencia de objetos de mensagem e padroniza saida textual.

Quando usar:

- Quando voce precisa quebrar uma tarefa em passos (ex.: traduzir e depois resumir).
- Para reaproveitar subchains em fluxos maiores.
- Em pipelines onde cada etapa exige um formato de entrada diferente.

## Como executar os exemplos

No diretorio raiz do projeto:

```bash
# 1) ativar ambiente virtual
source .venv/bin/activate

# 2) instalar dependencias
pip install -r requirements.txt

# 3) configurar variaveis de ambiente
cp .env.example .env
# preencher OPENAI_API_KEY e/ou GOOGLE_API_KEY

# 4) executar exemplos
python 3-chains-e-processamento/1-init-chains.py
python 3-chains-e-processamento/2-chains-com-decorators.py
python 3-chains-e-processamento/3-runneble-lambda.py
python 3-chains-e-processamento/4-pipeline-de-processamento.py
```

## Erros comuns e diagnostico rapido

- **KeyError em templates/chains**: confirme se as chaves retornadas por uma etapa existem na etapa seguinte.
- **Erro de autenticacao**: valide chaves no `.env` e permissao do provedor.
- **Tipo inesperado**: revise o retorno de funcoes `@chain` e `RunnableLambda`.
- **ImportError**: instale dependencias com `pip install -r requirements.txt`.

## Proximos passos sugeridos

Depois desta secao, voce pode evoluir para:

- parsers de saida estruturada;
- chains com branching e fallback;
- tools e agentes com fluxo mais complexo;
- RAG combinando retrieval + processamento + resposta final.
