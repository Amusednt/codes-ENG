import os
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain

# --- CONFIGURATION ---
# Ensure your OPENAI_API_KEY is set in your environment variables
# os.environ["OPENAI_API_KEY"] = "your-api-key-here"

def process_pdf(file_path):
    """
    Reads the PDF, splits text into chunks, and creates a searchable vector store.
    """
    print(f"Processing: {file_path}")
    
    # 1. Extract text using PyPDF2
    pdf_reader = PdfReader(file_path)
    raw_text = ""
    for page in pdf_reader.pages:
        content = page.extract_text()
        if content:
            raw_text += content

    # 2. Split text into manageable chunks for the LLM
    # 'chunk_overlap' helps maintain context between chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(raw_text)

    # 3. Create Embeddings and Vector Store (FAISS)
    # This allows us to perform semantic search over the PDF content
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(chunks, embeddings)
    
    return vector_store

def ask_question(vector_store, question):
    """
    Retrieves relevant chunks and sends them to OpenAI to answer the question.
    """
    # Perform a similarity search to find the most relevant parts of the PDF
    docs = vector_store.similarity_search(question)

    # Load the QA chain and run it
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    chain = load_qa_chain(llm, chain_type="stuff")
    
    response = chain.run(input_documents=docs, question=question)
    return response

if __name__ == "__main__":
    # Path to your large PDF file
    pdf_path = "document.pdf" 
    
    if os.path.exists(pdf_path):
        # Initial processing (Done once)
        knowledge_base = process_pdf(pdf_path)
        
        print("\nAI PDF Assistant is ready. Type 'exit' to quit.")
        while True:
            user_query = input("\nAsk a question about the PDF: ")
            if user_query.lower() == 'exit':
                break
            
            answer = ask_question(knowledge_base, user_query)
            print(f"\nAI: {answer}")
    else:
        print(f"Error: {pdf_path} not found.")
