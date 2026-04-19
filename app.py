import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import PyPDF2

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0F172A, #1E293B);
    color: white;
}

h1 {
    text-align: center;
    color: #F8FAFC;
    font-weight: 700;
}

h3 {
    text-align: center;
    color: #CBD5F5;
}

p, span, div {
    color: #E2E8F0 !important;
}

[data-testid="stFileUploader"] {
    background: #1E293B;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
}

button {
    background-color: #2563EB !important;
    color: white !important;
    border-radius: 10px !important;
}

[data-testid="stChatMessage"] {
    border-radius: 15px;
    padding: 12px;
}

[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
    background-color: #2563EB !important;
}

[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) {
    background-color: #1E293B !important;
}

.stChatInputContainer {
    background: #1E293B;
    border-radius: 12px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤖 AI Research Assistant")

st.markdown("""
<h3>🧠 Your Personal AI Research Assistant</h3>
<p style='text-align:center; color:#94A3B8;'>
Ask questions or upload research papers for quick insights.
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

st.markdown("### 📄 Upload Research Paper")

uploaded_file = st.file_uploader("", type=["pdf"])

if uploaded_file:
    text = extract_text(uploaded_file)

    if st.button("📌 Analyze Paper"):
        try:
            with st.spinner("Analyzing paper..."):
                response = model.generate_content(f"""
Analyze this research paper and provide:

- A short summary (max 5 sentences)
- Key contributions (2–3 bullet points)

Keep everything concise.

{text[:5000]}
""")
                st.subheader("📌 Research Paper Insights")
                st.write(response.text)
        except:
            st.error("⚠️ Error analyzing PDF.")

st.markdown("<br>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(msg)

user_input = st.chat_input("Ask your research question...")

if user_input:
    st.session_state.messages.append(("user", user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    prompt = f"""
You are an AI Research Assistant.

Answer the following question clearly and concisely.

STRICT RULES:
- Maximum 5 sentences
- No unnecessary explanation
- Be direct and simple

User Question:
{user_input}
"""

    try:
        with st.spinner("Thinking..."):
            response = model.generate_content(prompt)
            raw_reply = response.text.strip()

            # Enforce max 5 sentences strictly
            sentences = raw_reply.split(". ")
            bot_reply = ". ".join(sentences[:5])
            if not bot_reply.endswith("."):
                bot_reply += "."

    except:
        bot_reply = "⚠️ Error occurred. Please try again."

    st.session_state.messages.append(("assistant", bot_reply))

    with st.chat_message("assistant"):
        st.markdown(bot_reply)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("📥 Download Chat"):
    chat_text = "\n\n".join([f"{r.upper()}: {m}" for r, m in st.session_state.messages])
    st.download_button("Download", chat_text, file_name="chat.txt")
