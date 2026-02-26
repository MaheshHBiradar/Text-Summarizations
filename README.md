# Text-Summarizations

📋 Overview
This project provides multiple interfaces for content summarization and analysis:

🌐 Streamlit Web App (app.py) - Real-time summarization of YouTube videos and websites

📓 Research Assistant (tools_agents.ipynb) - Multi-tool research with Wikipedia, ArXiv, and custom retrieval

📄 Document Summarizer (text_summarization.ipynb) - Advanced PDF summarization with multiple techniques

✨ Key Features
🌐 Streamlit Summarizer
Multi-platform support: YouTube videos (with subtitles) and any website URL

Automatic language translation: Detects and translates non-English content

Real-time processing: Fast summaries using Groq's Llama 3.1 8B model

User-friendly interface: Clean, intuitive design with error handling

📚 Document Processing
PDF summarization using APJ Abdul Kalam's speeches as example

Multiple summarization techniques:

Stuff method: Simple, direct summarization

Map-Reduce: Process large documents by chunking

Refine chain: Iterative improvement for comprehensive summaries

🔬 Research Assistant
Wikipedia integration: Quick factual lookups

ArXiv search: Academic paper retrieval

Custom retriever: Vector store-based document search

Tool-using agents: Intelligent tool selection and execution

🛠️ Technology Stack
Component	Technology
Framework	LangChain 1.2.7
LLM Provider	Groq (Llama 3.1 8B)
Web Interface	Streamlit 1.53.1
Document Processing	PyPDF, Unstructured
Vector Store	FAISS
External APIs	Wikipedia, ArXiv, YouTube Transcript
Data Processing	Pandas, Numpy
