import os
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from dotenv import load_dotenv

load_dotenv()

# Azure OpenAI client
openai_client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-06-01"
)

# Azure AI Search client
search_client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name=os.getenv("AZURE_SEARCH_INDEX"),
    credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY"))
)


def chunk_text(text, chunk_size=800):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start += chunk_size
    return chunks


def get_embedding(text):
    response = openai_client.embeddings.create(
        model=os.getenv("EMBEDDING_MODEL_DEPLOYMENT"),
        input=text
    )
    return response.data[0].embedding


def process_file(filepath, category):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    chunks = chunk_text(text)
    docs = []
    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        doc = {
            "id": f"{os.path.splitext(os.path.basename(filepath))[0]}-{i}",
            "title": os.path.basename(filepath),
            "content": chunk,
            "category": category,
            "sourceFile": os.path.basename(filepath),
            "contentVector": embedding
        }
        docs.append(doc)
    return docs


def upload_documents(docs):
    result = search_client.upload_documents(documents=docs)
    print("Uploaded:", len(docs))


if __name__ == "__main__":

    all_docs = []

    all_docs += process_file("documents/vacation-policy.txt", "vacation")
    all_docs += process_file("documents/remote-work-policy.txt", "remote-work")
    all_docs += process_file("documents/benefits-overview.txt", "benefits")

    upload_documents(all_docs)

    print("Indexing complete")