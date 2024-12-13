from langchain_mistralai.chat_models import ChatMistralAI
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.document_loaders import PyMuPDFLoader
import streamlit as st

def get_response(question,key_1,key_2):
    loader = PyMuPDFLoader("./test.pdf",)
    docs = loader.load()
    # Split text into chunks 
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documents = text_splitter.split_documents(docs)
    # Define the embedding model
    embeddings=CohereEmbeddings(cohere_api_key=key_1, model="embed-english-v3.0")
    # Create the vector store 
    vector = FAISS.from_documents(documents, embeddings)
    # Define a retriever interface
    retriever = vector.as_retriever()
    # Define LLM
    model = ChatMistralAI(mistral_api_key=key_2)
    # Define prompt template
    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context based on the predefined embeddings only also mention the page numbers:
        <context>
        {context}
        </context>

        Question: {input}""")
    # Create a retrieval chain to answer questions
    document_chain = create_stuff_documents_chain(model, prompt)
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({"input" : question})
    return response["answer"]

# Page title
st.set_page_config(page_title='🔗 Chat with pdf')
st.title('🔗 Chat with pdf')

# File upload
uploaded_file = st.file_uploader('Upload an article', type='pdf')

# Query text
query_text = st.text_input('Enter your question:', placeholder = 'Please provide a short summary.', disabled=not uploaded_file)
api_1 = st.text_input('Enter your Cohere Embedding API Key: ', placeholder = 'Please enter the key', disabled=not uploaded_file)
api_2 = st.text_input('Enter your Mistral LLM API Key:', placeholder = 'Please provide enter the key.', disabled=not uploaded_file)

# Form input and query
result = []
with st.form('myform', clear_on_submit=True):
    submitted = st.form_submit_button('Submit', disabled=not(uploaded_file and query_text))
    if submitted:
        with st.spinner('Calculating...'):
            with open("./test.pdf", "wb") as file:
                file.write(uploaded_file.getvalue())
            response = get_response(query_text,api_1,api_2)
            result.append(response)

if len(result):
    st.info(response)
