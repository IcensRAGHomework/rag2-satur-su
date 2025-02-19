from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    docs = loader.load()
    return docs[len(docs) - 1]

def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    docs = loader.load()
    text = ""
    for doc in docs:
        text = text + doc.page_content + "\n"
    spliter = RecursiveCharacterTextSplitter(separators=["[ \n]第.*[章條][ \n]"],
        chunk_size=0,
        chunk_overlap=0,
        is_separator_regex=True,
        keep_separator=True)
    result = spliter.create_documents([text])
    return(len(result))

print(hw02_2(q2_pdf))
