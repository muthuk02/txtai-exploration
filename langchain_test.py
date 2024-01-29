from langchain_community.llms.ctransformers import CTransformers
from langchain.chains import NebulaGraphQAChain
from langchain_community.graphs import NebulaGraph


llm = CTransformers(model='models\llama-2-13b-chat.Q4_K_M.gguf', model_type='llama')

print(llm('Who is Rajinikanth?'))


