from fastapi import FastAPI, UploadFile, File
import shutil
from rag_pipeline import load_pdf, split_docs, create_vectorstore, ask_question

app = FastAPI()

vectorstore = None


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global vectorstore

    with open("temp.pdf", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    docs = load_pdf("temp.pdf")
    chunks = split_docs(docs)
    vectorstore = create_vectorstore(chunks)

    return {"message": "PDF processed successfully"}


@app.get("/ask")
def ask(query: str):
    global vectorstore

    if vectorstore is None:
        return {"error": "Upload a PDF first"}

    return ask_question(vectorstore, query)
