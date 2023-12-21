import os
from langchain.document_loaders import ReadTheDocsLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS


def ingest_doc() -> None:
    loader = ReadTheDocsLoader(
        path="D:\\LangChain\\documentation-helper\\documentation-helper\\sbert\\content\\www.sbert.net",
        encoding="utf-8",
    )
    raw_documents = loader.load()
    print(f"loaded {len(raw_documents)} documents.")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=100, separators=["\n\n", "\n", "", " "]
    )
    documents = text_splitter.split_documents(documents=raw_documents)
    print(f"Splitted into {len(documents)} chunks.")
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(documents, embeddings)
    vector_store.save_local("faiss_index_dochelper")
    print("Data is added to FAISS.")


if __name__ == "__main__":
    ingest_doc()
