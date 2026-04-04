import urllib.request, urllib.error, os, sys
from dotenv import load_dotenv
load_dotenv()

base = os.getenv('AZURE_OPENAI_ENDPOINT').rstrip('/')
key = os.getenv('AZURE_OPENAI_API_KEY')
print(f"Base: {base}", flush=True)

from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=key,
    azure_endpoint='https://aoai-rag-lab-boud0217.openai.azure.com',
    api_version='2024-06-01'
)

try:
    r = client.embeddings.create(model=os.getenv('EMBEDDING_MODEL_DEPLOYMENT'), input='test')
    print(f"Success! Embedding length: {len(r.data[0].embedding)}", flush=True)
except Exception as e:
    print(f"Error: {e}", flush=True)

sys.stdout.flush()
