import streamlit as st
from utils import *
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Main function 
def main():

    # Streamlit interface
    st.set_page_config(page_title="PDF Summarizer", layout="wide")

    # Header
    st.title("📄 PDF Summarizer")
    st.write("Upload your PDF file to extract and summarize its content.")

    # File uploader
    pdf_file = st.file_uploader("Upload your PDF file here", type="pdf")
    submit = st.button("Generate Summary")

    # Check if the OpenAI API key is available
    if openai_api_key:
        st.write("OpenAI API Key Loaded")
    else:
        st.error("OpenAI API Key is missing! Please set it up.")

    if submit:
        with st.spinner("Processing..."):
        
            response = summarizer(pdf_file)
        
            st.subheader("Summary of the file:")
            st.write(response)


    # Footer
    st.markdown(
        """
        ---
        Made with ❤️ by [Hamza Aamir](https://hamzaaamir.vercel.app)
        """
    )

if __name__ == "__main__":
    main()
