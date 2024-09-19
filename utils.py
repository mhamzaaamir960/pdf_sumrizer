# import pakages

from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from PyPDF2 import PdfReader


# Function to process the text
def process_text(text):
    
    # Text splitter to divide the text into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    
    # Split text into chunks
    chunks = text_splitter.split_text(text)
    
    # Generating embeddings using HuggingFace
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Create the FAISS index from the text chunks using embeddings
    faiss_index = FAISS.from_texts(chunks, embeddings)
    
    return faiss_index


# Function to summarize the content of a PDF file
def summarizer(pdf):
    
    if pdf is not None:
        
        pdf_reader = PdfReader(pdf)
        text = ""
        
        for page_num in range(len(pdf_reader.pages)):
            page_text = pdf_reader.pages[page_num].extract_text()
            if page_text:  # Ensure extracted text is not None
                text += page_text
            
        if not text:
            return "The PDF contains no extractable text."
        
        # Process the extracted text to create a knowledge base
        faiss_index = process_text(text)
        
        # Query for summarization
        query = "Summarize the content of the uploaded pdf file in approximately 5-10 sentences."
        
        # Perform similarity search on the FAISS index
        docs = faiss_index.similarity_search(query)
        
        # Specify the OpenAI model for generating the summary
        openai_model = "gpt-3.5-turbo-16k"
        llm = ChatOpenAI(model_name=openai_model, temperature=0.1)
        
        # Load a question answering chain with the specified model
        chain = load_qa_chain(llm, chain_type='stuff')
        
        # Run the chain to get a response
        response = chain.run(input_documents=docs, question=query)
        
        # Return the summary of the file
        return response
    
    return "No PDF uploaded."
