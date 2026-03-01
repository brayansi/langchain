# Chains e Processamento no LangChain

Esta seção consolida os estudos de encadeamento e transformação de dados com LCEL no projeto.
O objetivo é mostrar como combinar etapas com o operador `|`, criar funções reutilizáveis e processar entrada/saída com runnables.

Arquivos cobertos nesta seção:

- `1-init-chains.py`
- `2-chains-com-decorators.py`
- `3-runneble-lambda.py`
- `4-pipeline-de-processamento.py`
- `5-sumarizacao.py`
- `6-sumarizacao-com-map-reduce.py`
- `7-sumarizacao-com-map-reduce.py`

## 1) Encadeamento básico com `PromptTemplate | model`

Arquivo: `3-chains-e-processamento/1-init-chains.py`

Nesse exemplo, você:

1. Carrega variáveis de ambiente com `load_dotenv()`.
2. Cria um `PromptTemplate` com variável dinâmica (`topic`).
3. Inicializa o modelo com `ChatOpenAI`.
4. Encadeia `template | model` para formar uma chain simples.
5. Executa com `invoke(...)` e imprime `response.content`.

Conceitos-chave:

- **LCEL (`|`)**: conecta componentes de forma declarativa, onde a saída de uma etapa alimenta a próxima.
- **`invoke`**: executa a cadeia inteira em uma chamada síncrona.
- **Composição simples**: bom ponto de partida para pipelines pequenos.

Quando usar:

- Geração de texto a partir de um prompt parametrizado.
- Fluxos de uma única etapa de transformação + inferência.
- Teste rápido de prompts reaproveitáveis.

## 2) Chain customizada com decorator `@chain`

Arquivo: `3-chains-e-processamento/2-chains-com-decorators.py`

Esse exemplo adiciona uma etapa Python antes do prompt:

1. Define uma função com `@chain` para processar dados de entrada.
2. A função recebe `{ "x": ... }` e retorna `{ "squere_result": ... }`.
3. O resultado alimenta o `PromptTemplate`.
4. O modelo recebe o prompt final e gera a resposta.

Conceitos-chave:

- **`@chain`**: transforma função Python em runnable compatível com LCEL.
- **Pre-processamento**: permite calcular/normalizar dados antes da chamada ao LLM.
- **Contrato de dados entre etapas**: chaves de entrada e saída precisam estar alinhadas.

Quando usar:

- Fluxos com regra de negócio antes do LLM.
- Casos em que você quer separar transformação de dados e geração de texto.
- Pipelines com mais controle sobre o formato de entrada.

## 3) Conversão de tipo com `RunnableLambda`

Arquivo: `3-chains-e-processamento/3-runneble-lambda.py`

Esse exemplo mostra uma transformação isolada:

1. Cria a função `parse_number(text: str) -> int`.
2. Encapsula a função com `RunnableLambda`.
3. Executa com `invoke("10")`.
4. Retorna `int` em vez de `str`.

Conceitos-chave:

- **`RunnableLambda`**: adapta funções Python para o ecossistema de runnables.
- **Transformação de entrada/saída**: útil para preparar dados entre etapas.
- **Reuso composicional**: funções pequenas podem ser combinadas em chains maiores.

Quando usar:

- Parsing de dados recebidos como texto.
- Normalização e validação antes de prompts/modelos.
- Composição de pipelines com etapas técnicas e sem LLM.

## 4) Pipeline de processamento com tradução + resumo

Arquivo: `3-chains-e-processamento/4-pipeline-de-processamento.py`

Esse exemplo monta um fluxo em duas etapas com parser de saída:

1. Cria um prompt para tradução (`initial_text -> text em inglês`).
2. Encadeia o modelo com `StrOutputParser()` para garantir retorno em `str`.
3. Usa a saída da tradução como entrada de um segundo prompt de resumo.
4. Gera a resposta final com outro `StrOutputParser()`.

Conceitos-chave:

- **Pipeline com múltiplas etapas**: combina transformação intermediária e resultado final.
- **Mapeamento de entrada com dict runnable**: `{ "text": translate }` conecta a saída de uma subchain a outra etapa.
- **`StrOutputParser`**: remove dependência de objetos de mensagem e padroniza saída textual.

Quando usar:

- Quando você precisa quebrar uma tarefa em passos (ex.: traduzir e depois resumir).
- Para reaproveitar subchains em fluxos maiores.
- Em pipelines onde cada etapa exige um formato de entrada diferente.

## 5) Sumarização com `stuff` via `load_summarize_chain`

Arquivo: `3-chains-e-processamento/5-sumarizacao.py`

Esse exemplo usa uma API utilitária pronta de sumarização:

1. Divide um texto longo em partes com `RecursiveCharacterTextSplitter`.
2. Inicializa um `ChatOpenAI`.
3. Cria a chain com `load_summarize_chain(..., chain_type="stuff")`.
4. Invoca com `{"input_documents": parts}` e imprime o resumo.

Conceitos-chave:

- **`stuff`**: concatena os documentos e gera um único resumo final.
- **API utilitária de chains**: reduz boilerplate para resumos diretos.
- **Segmentação de contexto**: mantém o input organizado para a etapa de resumo.

Quando usar:

- Para estudar exemplos existentes com `load_summarize_chain`.
- Quando você quer um fluxo simples com pouca configuração.
- Como referência antes de customizar o pipeline com LCEL.

## 6) Sumarização com `map_reduce` via `load_summarize_chain`

Arquivo: `3-chains-e-processamento/6-sumarizacao-com-map-reduce.py`

Esse exemplo usa uma API utilitária para `map_reduce`:

1. Segmenta o texto em documentos com `RecursiveCharacterTextSplitter`.
2. Inicializa um `ChatOpenAI`.
3. Cria a chain com `load_summarize_chain(..., chain_type="map_reduce")`.
4. Executa com `{"input_documents": parts}` para combinar resumo por etapas.

Conceitos-chave:

- **`map_reduce`**: resume partes separadas e depois consolida em um resumo final.
- **Escalabilidade de contexto**: funciona melhor que `stuff` em textos maiores.
- **Implementação pronta**: acelera a construção de resumo em múltiplas etapas.

Quando usar:

- Para comparar `stuff` vs `map_reduce` em exemplos didáticos.
- Para textos maiores onde uma única concatenação pode degradar o resultado.
- Quando você quer escalar a sumarização sem montar o pipeline manualmente.

## 7) Sumarização com map-reduce em LCEL

Arquivo: `3-chains-e-processamento/7-sumarizacao-com-map-reduce.py`

Esse exemplo implementa map-reduce no padrão moderno:

1. Cria um estágio `map` com `PromptTemplate | llm | StrOutputParser`.
2. Executa o `map` em cada chunk com `map_chain.map()`.
3. Prepara os resumos parciais com `RunnableLambda`.
4. Aplica um estágio `reduce` para consolidar o resumo final.

Conceitos-chave:

- **LCEL composável**: cada etapa fica explícita e fácil de evoluir.
- **`RunnableLambda`**: organiza os dados entre map e reduce.
- **Pipeline declarativo**: expõe cada etapa para customização completa.

Quando usar:

- Em projetos novos no ecossistema LangChain.
- Quando você quer controle detalhado das etapas de sumarização.
- Para adaptar prompts diferentes no map e no reduce.

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
python 3-chains-e-processamento/1-init-chains.py
python 3-chains-e-processamento/2-chains-com-decorators.py
python 3-chains-e-processamento/3-runneble-lambda.py
python 3-chains-e-processamento/4-pipeline-de-processamento.py
python 3-chains-e-processamento/5-sumarizacao.py
python 3-chains-e-processamento/6-sumarizacao-com-map-reduce.py
python 3-chains-e-processamento/7-sumarizacao-com-map-reduce.py
```

## Erros comuns e diagnóstico rápido

- **KeyError em templates/chains**: confirme se as chaves retornadas por uma etapa existem na etapa seguinte.
- **Erro de autenticação**: valide chaves no `.env` e permissão do provedor.
- **Tipo inesperado**: revise o retorno de funções `@chain` e `RunnableLambda`.
- **ImportError**: instale dependências com `pip install -r requirements.txt`.
- **Erro com `stuff`/`load_summarize_chain`**: valide o formato de entrada (`input_documents`) e compare com a abordagem LCEL do `7-sumarizacao-com-map-reduce.py`.

## Próximos passos sugeridos

Depois desta seção, você pode evoluir para:

- parsers de saída estruturada;
- chains com branching e fallback;
- tools e agentes com fluxo mais complexo;
- RAG combinando retrieval + processamento + resposta final.
