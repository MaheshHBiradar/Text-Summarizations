import validators
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

# Streamlit APP Configuration
st.set_page_config(page_title="AI Summarizer: YouTube & Web", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')

# Sidebar for Groq API Key
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")
    st.info("Note: For YouTube videos, ensure Subtitles/CC are available.")

# URL Input
generic_url = st.text_input("URL", label_visibility="collapsed")

# Define the Summarization Prompt
# Added instruction to translate to English if the content is in another language
prompt_template = """
Summarize the following content in about 300 words. 
If the content is not in English, please translate your summary into English:
Content: {text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

if st.button("Summarize Content"):
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide both the Groq API Key and the URL.")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL.")
    else:
        try:
            with st.spinner("Extracting and Summarizing..."):
                # 1. Initialize the Groq LLM
                llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=groq_api_key)

                # 2. Load Data from YouTube or Website
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    # FIX: Simplified language list and removed 'translation' parameter
                    # This often bypasses 'Blocked' errors by reducing API complexity
                    loader = YoutubeLoader.from_youtube_url(
                        generic_url, 
                        add_video_info=False,
                        language=["hi", "en"] # Tries Hindi first, then English
                    )
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url], 
                        ssl_verify=False,
                        headers={"User-Agent": "Mozilla/5.0"}
                    )
                
                docs = loader.load()
                
                if not docs:
                    st.error("No content found. The video might not have transcripts enabled.")
                else:
                    combined_text = " ".join([doc.page_content for doc in docs])
                    
                    # 3. Chain logic (LCEL)
                    chain = prompt | llm | StrOutputParser()
                    output_summary = chain.invoke({"text": combined_text})
                    
                    st.success("### Summary:")
                    st.write(output_summary)

        except Exception as e:
            error_msg = str(e)
            if "Cookies" in error_msg or "blocked" in error_msg.lower():
                st.error("YouTube is blocking the automated request. Try again in a few minutes or try a different video.")
            elif "No transcripts" in error_msg:
                st.error("This video does not have any captions/transcripts available.")
            else:
                st.error(f"Error: {e}")