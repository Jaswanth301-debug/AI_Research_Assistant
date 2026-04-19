# 🤖 AI Research Assistant (Live Web App)

An AI-powered research assistant built using **Streamlit** and **Google Gemini API** that helps users quickly understand AI/ML concepts and analyze research papers with concise responses.

---

## 🚀 Live Demo

👉 *https://airesearchassistant-wfkzinqmfzeqdfvehzvjhm.streamlit.app/*

---

## 📌 Features

* 💬 **Chat-based AI Assistant**
  Ask questions related to AI, Machine Learning, Deep Learning, and get clear answers.

* 📄 **Research Paper Analyzer**
  Upload a PDF and get:

  * Short summary
  * Key contributions

* 🎨 **Modern UI**
  Clean dark-themed interface with chat-style interaction.

* 💾 **Download Chat History**
  Save your conversation for later use.

---

## 🧠 Tech Stack

* **Frontend/UI:** Streamlit
* **AI Model:** Google Gemini (gemini-2.5-flash)
* **Backend:** Python
* **Libraries:**

  * google-generativeai
  * PyPDF2
  * python-dotenv

---

## 📂 Project Structure

```
AI-Research-Assistant/
│── app.py
│── requirements.txt
│── .gitignore
```

---

## ⚙️ Installation (Run Locally)

### 1. Clone the repository

```
git clone https://github.com/Jaswanth301-debug/AI_Research_Assistant.git
cd ai-research-assistant
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add API Key

Create a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

---

### 5. Run the app

```
streamlit run app.py
```

---

## ☁️ Deployment

This app is deployed using **Streamlit Cloud**.

Steps:

1. Push code to GitHub
2. Connect repo to Streamlit Cloud
3. Add `GOOGLE_API_KEY` in **Secrets**
4. Deploy

---

## 🎯 Use Cases

* Quick AI/ML concept understanding
* Research paper summarization
* Study assistant for students
* Idea exploration for projects

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* Streamlit
* Google Gemini API

