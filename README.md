# 📄 LangChain PDF QA Bot

This project is a **Question-Answering Bot** built using **LangChain**, **OpenAI embeddings/LLM**, and **Qdrant** as a vector store. It allows users to ask natural language questions, and it answers based on the content of a local PDF document.

> ⚠️ The sample PDF file (`sample.pdf`) is **not uploaded to this repository**. Please add your own PDF file in the root directory for testing.

---

## 🚀 Features

- ✅ Load and parse PDF using LangChain's `PyPDFLoader`
- ✅ Split text into manageable chunks for semantic search
- ✅ Embed using OpenAI's `text-embedding-3-small`
- ✅ Store and retrieve vectors from **Qdrant**
- ✅ Use GPT-4o (or any OpenAI chat model) to answer questions from retrieved context
- ✅ Interactive CLI for asking questions in a loop

---

## 📁 Project Structure

```
pdf_qa_langchain/
├── main.py           # Main script to run the QA bot
├── .env              # Contains your OpenAI API key (excluded via .gitignore)
├── .gitignore        # Ensures .env and __pycache__ are not committed
├── requirements.txt  # Required Python packages
├── README.md         # This file
└── sample.pdf        # Your PDF file (NOT included in this repo)
```

---

## ⚙️ Setup Instructions

### 1. 🔑 Create `.env`

In the root folder, create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 2. 📦 Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

Then install required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Make sure you have a **Qdrant instance running** locally at `http://localhost:6333` (e.g., via Docker).

Then run:

```bash
python main.py
```

You will be prompted to enter a question. The model will search your PDF content and answer based on the most relevant sections.

---

## 🧠 Tech Stack

- [LangChain](https://www.langchain.com/)
- [OpenAI API](https://platform.openai.com/)
- [Qdrant Vector Store](https://qdrant.tech/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

---
