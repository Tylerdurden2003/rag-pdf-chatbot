import streamlit as st
import requests

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="RAG Chatbot", layout="wide")

# -----------------------------
# CUSTOM CSS (PREMIUM LOOK)
# -----------------------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}

.chat-bubble-user {
    background-color: #2563eb;
    color: white;
    padding: 12px;
    border-radius: 15px;
    margin: 5px;
    text-align: right;
}

.chat-bubble-bot {
    background-color: #1e293b;
    color: white;
    padding: 12px;
    border-radius: 15px;
    margin: 5px;
    text-align: left;
}

.sidebar-content {
    font-size: 14px;
    color: #cbd5f5;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.title("📄 RAG Chatbot")
    st.markdown(
        "<div class='sidebar-content'>Upload a PDF and ask questions about it.</div>",
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

    if uploaded_file:
        files = {
            "file": (uploaded_file.name, uploaded_file, "application/pdf")
        }

        res = requests.post("http://127.0.0.1:8000/upload", files=files)

        if res.status_code == 200:
            st.success("PDF uploaded!")

# -----------------------------
# CHAT STATE
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# TITLE
# -----------------------------
st.title("🤖 Ask your PDF")

# -----------------------------
# CHAT DISPLAY
# -----------------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"<div class='chat-bubble-user'>{msg['content']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='chat-bubble-bot'>{msg['content']}</div>",
            unsafe_allow_html=True
        )

# -----------------------------
# INPUT
# -----------------------------
query = st.chat_input("Type your question...")

if query:
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    # Spinner + API call
    with st.spinner("Thinking..."):
        res = requests.get(
            "http://127.0.0.1:8000/ask",
            params={"query": query}
        )

        if res.status_code == 200:
            data = res.json()

            answer = data.get("answer", "No answer")
            sources = data.get("sources", [])

            # Format sources nicely
            source_text = "\n".join([f"• Page {s}" for s in sources])

            full_response = f"{answer}\n\n**Sources:**\n{source_text}"

        else:
            full_response = "⚠️ Backend error"

    # Add bot message
    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response
    })

    st.rerun()
