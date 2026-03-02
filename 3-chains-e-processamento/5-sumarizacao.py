from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
load_dotenv()

long_text = """
O amanhecer derrama uma luz dourada entre os prédios de vidro.
A cidade desperta em um coro de freios e sirenes distantes.
Janelas se acendem uma a uma, como olhos sonolentos.
Vapores sobem dos bueiros e desenham rios no asfalto.
Pedestres apressados cruzam as calçadas com guarda-chuvas coloridos.
Os ônibus engolem a manhã com seu ronco pesado.
Uma bicicleta corta o trânsito, brilhando em velocidade.
O metrô respira no subterrâneo como um coração constante.
Padarias exalam cheiro de pão quente e café recém-passado.
Vendedores de rua gritam ofertas em diferentes sotaques.
Pombos disputam migalhas entre passos acelerados.
Arranha-céus tocam nuvens enquanto os trens seguem nos túneis.
A cidade pulsa com milhões de sonhos e prazos.
Do amanhecer ao anoitecer, a orquestra urbana não para.
É uma canção contínua de trabalho, luta e esperança.
"""

splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=70)
parts = splitter.create_documents([long_text])
llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
chain_sumarize = load_summarize_chain(llm, chain_type="stuff", verbose=False)

result = chain_sumarize.invoke({"input_documents": parts})

print(result["output_text"])