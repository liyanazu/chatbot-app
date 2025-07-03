import streamlit as st
import requests

# ==== CONFIGURATION ====
N8N_WEBHOOK_URL = "https://c13f-202-188-232-143.ngrok-free.app/webhook/rag-chat"
# This matches your active n8n webhook

# ==== UI ====
st.title("💬 My RAG Chatbot")
st.write("Ask me anything about our documents or knowledge base.")

# Chat input (Streamlit >=1.25 has st.chat_input)
query = st.chat_input("Type your question here...")
if not query:
    query = st.text_input("Or type your question here:")

# ==== Send to backend ====
if query:
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                N8N_WEBHOOK_URL,
                json={"question": query}
            )
            if response.ok:
                data = response.json()
                answer = data.get("answer", "⚠️ No 'answer' field returned by n8n.")
                st.markdown(f"**Answer:** {answer}")
            else:
                st.error(f"🚨 n8n returned error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"🚨 Failed to reach n8n backend: {e}")
