from huggingface_hub import InferenceClient
import json

repo_id='microsoft/Phi-3-mini-4k-instruct'

llm_client=InferenceClient(model=repo_id,timeout=120,)

def call_llm(inference_client:InferenceClient,prompt:str):
    response=inference_client.post(
        json={
            'inputs':prompt,
            'parameters':{'max_new_tokens':200},
            'task':'text-generation',
        },
    )
    return json.loads(response.decode())[0]['generated_text']
response=call_llm(llm_client,'Give a python code for implementing linear regression')
print(response)