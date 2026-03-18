# 🧠 RAG PDF Chatbot

An AI-powered chatbot that allows users to upload PDFs and ask questions about their content in natural language.
Built using Retrieval-Augmented Generation (RAG), this system combines document understanding with LLM-based reasoning.

---

## 🚀 Features

* 📄 Upload and analyze any PDF
* 💬 Ask questions in natural language
* 🧠 Context-aware answers using RAG pipeline
* 🔍 Displays source references (page numbers)
* ⚡ Fast semantic search using vector embeddings
* 🌐 Clean ChatGPT-style UI
* ☁️ Backend deployed with API support

---

## 🧩 How It Works

1. **PDF Upload**

   * The document is loaded and processed using a PDF parser.

2. **Text Chunking**

   * Content is split into smaller chunks for better retrieval.

3. **Embedding Generation**

   * Each chunk is converted into vector embeddings using OpenAI models.

4. **Vector Storage**

   * Embeddings are stored using FAISS for efficient similarity search.

5. **Query Handling**

   * User query is embedded and matched against stored chunks.

6. **Response Generation**

   * Relevant chunks are passed to an LLM to generate a contextual answer.

---

## 🛠️ Tech Stack

**Frontend**

* Streamlit

**Backend**

* FastAPI

**AI / NLP**

* LangChain
* OpenAI API

**Vector Database**

* FAISS

**Other Tools**

* Python
* dotenv (environment management)

---

## 📁 Project Structure

```
rag-chatbot-deploy/
│
├── backend/
│   ├── main.py
│   ├── rag_pipeline.py
│   ├── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-pdf-chatbot.git
cd rag-pdf-chatbot
```

---

### 2. Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

Run backend:

```bash
uvicorn main:app --reload
```

---

### 3. Frontend Setup

```bash
cd ../frontend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Run frontend:

```bash
streamlit run app.py
```

---

## 🌍 Deployment

* Backend deployed on Render
* Frontend can be deployed on Streamlit Cloud

---

## 💡 Key Learnings

* Understanding of RAG (Retrieval-Augmented Generation)
* Working with vector databases and embeddings
* Backend API design using FastAPI
* Handling real-world deployment issues
* Integrating LLMs into full-stack applications

---

## 📌 Future Improvements

* Add user authentication
* Persistent chat history
* Use advanced vector DB (Pinecone / Chroma)
* Improve UI with React
* Add multi-document support

---

## 🤝 Author

**Abhinav Gopal**
🔗 GitHub: https://github.com/Tylerdurden2003

---

## ⭐ Final Note

This project was built to explore how AI can interact with real-world documents.
It demonstrates practical implementation of modern LLM-based systems beyond simple chat interfaces.
