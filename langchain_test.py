from langchain_community.llms.ctransformers import CTransformers
from langchain.chains import NebulaGraphQAChain
from langchain_community.graphs import NebulaGraph

config = {'context_length':4092, 'max_new_tokens':512, 'repetition_penalty':1.1, 'temperature':0}

llm = CTransformers(model='models/zephyr-7b-alpha.Q4_K_M.gguf', model_type='llama', config=config)

print(llm('What is the capital of Canada?'))


