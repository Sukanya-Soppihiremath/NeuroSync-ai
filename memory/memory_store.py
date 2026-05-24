import chromadb

client = chromadb.Client()

collection = client.create_collection(
    name="neurosync"
)


def save_memory(user, response):

    collection.add(
        documents=[
            f"""User: {user} 
            AI: {response}"""
        ],
        ids=[str(hash(user))]
    )


def search_memory(query):

    result=collection.query(

        query_texts=[query],

        n_results=3
    )

    return result
