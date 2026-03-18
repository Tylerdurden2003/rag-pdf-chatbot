from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
load_dotenv()


def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()


def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_documents(docs)


def create_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore


def ask_question(vectorstore, query):
    retriever = vectorstore.as_retriever()

    # Retrieve relevant chunks
    docs = retriever.invoke(query)

    # Build sources (FIXED)
    sources = []
    for i, doc in enumerate(docs):
        page = doc.metadata.get("page")

        if page is None:
            sources.append(f"Chunk {i}")
        else:
            sources.append(page + 1)

    # Remove duplicates
    sources = list(set(sources))

    # Build context
    context = "\n".join([doc.page_content for doc in docs])

    # LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo")

    # Prompt
    prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": sources
    }
