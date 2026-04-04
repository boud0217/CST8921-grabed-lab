import os
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from dotenv import load_dotenv

load_dotenv()

openai_client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-06-01"
)

search_client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name=os.getenv("AZURE_SEARCH_INDEX"),
    credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY"))
)


def get_embedding(text):
    response = openai_client.embeddings.create(
        model=os.getenv("EMBEDDING_MODEL_DEPLOYMENT"),
        input=text
    )
    return response.data[0].embedding


def print_results(label, results):
    print(f"\n{'='*60}")
    print(f" {label}")
    print(f"{'='*60}")
    for r in results:
        print(f"{r['title']}")
        print(f"  {r['content'][:150].strip()}")
        print()


QUERY = "vacation carryover"

# A. Keyword Search
keyword_results = search_client.search(
    search_text=QUERY,
    select=["title", "content"]
)
print_results("A. Keyword Search", keyword_results)

# B. Vector Search
embedding = get_embedding(QUERY)
vector_query = VectorizedQuery(
    vector=embedding,
    k_nearest_neighbors=3,
    fields="contentVector"
)
vector_results = search_client.search(
    search_text=None,
    vector_queries=[vector_query],
    select=["title", "content"]
)
print_results("B. Vector Search", vector_results)

# C. Hybrid Search
hybrid_results = search_client.search(
    search_text=QUERY,
    vector_queries=[vector_query],
    select=["title", "content"]
)
print_results("C. Hybrid Search", hybrid_results)
