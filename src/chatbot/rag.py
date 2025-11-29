# NOTE: This is a scaffold. Set OPENAI_API_KEY env var before use.
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from pathlib import Path

REPORTS_DIR = Path('reports/text')

def build_vectorstore_from_texts(report_paths=None):
    if report_paths is None:
        report_paths = list(REPORTS_DIR.glob('*.txt'))
    docs = []
    for p in report_paths:
        loader = TextLoader(str(p))
        docs.extend(loader.load())
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    embed = OpenAIEmbeddings()
    store = FAISS.from_documents(chunks, embed)
    return store

def make_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={'k': 4})
    llm = ChatOpenAI(temperature=0)
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=retriever)
    return qa
