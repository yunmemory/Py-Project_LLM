# ------------------------ importing ------------------------ #
import os
import openai
from dotenv import load_dotenv
import numpy as np

# import PyPDFLoader from langchain
from langchain.document_loaders import PyPDFLoader, UnstructuredMarkdownLoader, TextLoader

# import autoloader from langchain
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser

# import WebBasedLoader from langchain
from langchain.document_loaders.web_base import WebBaseLoader

# import data from Notion
from langchain.document_loaders import NotionDBLoader

# import openai embedding
from langchain.embeddings.openai import OpenAIEmbeddings

# import vectorstore
from langchain.vectorstores import Chroma
persist_dir = r"C:\Users\ROG\Downloads\langchain_test\vectorstore"

# ------------------------ end of importing ------------------------ #

# ------------------------ set reference ------------------------ #
# load the .env file
load_dotenv()

# reference
PDF_File = r"C:\Users\ROG\Downloads\1-s2.0-S0926580515000370-main.pdf"
Notion_DB = "https://www.notion.so/a11ab2438d224563a4997fd73ed15f97?v=eed6f674983f43fd98c478e9a3db5ac5&pvs=4"
Youtube_url = "https://www.youtube.com/watch?v=KwAXfey-xQk"
Page_URL = "https://python.langchain.com/docs/get_started/introduction"
Save_dir = r"C:\Users\ROG\Downloads\langchain_test"
md_docs = "./天源石化-员工手册_all_headings.md"

# get the api key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# get notion token and database id
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

# ------------------------ end of set reference ------------------------ #

# ------------------------ Start of file loading ------------------------ #

# # load the pdf file
# pdf_loader = PyPDFLoader(PDF_File)
# pages = pdf_loader.load()
# page = pages[0]
#
# # print(page.page_content[0:500])
# data = page.metadata
# print(data)

# # load the youtube video
# youtube_loader = GenericLoader(YoutubeAudioLoader([Youtube_url], Save_dir), OpenAIWhisperParser())
# docs = youtube_loader.load()
# print(docs[0].page_content[0:500])

# # load the web page
# web_loader = WebBaseLoader(Page_URL)
# web_pages = web_loader.load()
# print(web_pages[0])

# # load the notion database
# notion_loader = NotionDBLoader(
#     integration_token=NOTION_TOKEN,
#     database_id=DATABASE_ID,
#     request_timeout_sec=30,  # optional, defaults to 10
# )
# notion_pages = notion_loader.load()
# print(notion_pages)

# # markdown loader
# mark_down_loader = UnstructuredMarkdownLoader(md_docs, mode="elements")
# md_pages = mark_down_loader.load()

# text loader
text_loader = TextLoader(md_docs, encoding="utf-8")
text_pages = text_loader.load()

# initialize the openai embedding
openai_embedding = OpenAIEmbeddings()

# ------------------------ End of file loading ------------------------ #

# ------------------------ Start of document splitting ------------------------ #
# Document Spliction
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter, TokenTextSplitter, \
    MarkdownHeaderTextSplitter

chunk_size = 20
chunk_overlap = 5
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separators=["\n\n", "\n", "(?<=\. )", " "]  # split on double newlines, newlines, and periods
)
c_splitter = CharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separator=" ",
    length_function=len
)
t_splitter = TokenTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)
m_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

# ------------------------ End of document splitting ------------------------ #

# ------------------------ Start of samples ------------------------ #
# # split the text
text = "a b c d e f g h i j k l m n o p q r s t u v w x y z"

markdown_document = """# Title\n\n \
## Chapter 1\n\n \
Hi this is Jim\n\n Hi this is Joe\n\n \
### Section \n\n \
Hi this is Lance \n\n 
## Chapter 2\n\n \
Hi this is Molly"""

# embedding samples
sentence1 = "i like dogs"
sentence2 = "i like canines"
sentence3 = "the weather is ugly outside"

# ------------------------ End of samples ------------------------ #


# ------------------------ Start of chunks ------------------------ #
# join the pages in md_pages into a single string
md_text = "/n".join([d.page_content for d in text_pages])

# r_chunks = r_splitter.split_text(some_text)
# c_chunks = c_splitter.split_documents(pages)
# t_chunks = t_splitter.split_text(some_text)
md_chunks = m_splitter.split_text(md_text)

# ------------------------ End of chunks ------------------------ #

# ------------------------ Start of embedding ------------------------ #
# embedding
embedding1 = openai_embedding.embed_query(sentence1)
embedding2 = openai_embedding.embed_query(sentence2)
embedding3 = openai_embedding.embed_query(sentence3)

# print(np.dot(embedding1, embedding2))
# print(np.dot(embedding1, embedding3))
# print(np.dot(embedding2, embedding3))

vectordb = Chroma.from_documents(
    documents=md_chunks,
    embedding=openai_embedding,
    persist_directory=persist_dir
)

question = "天源员工手册第一章讲的什么内容？"
question_fail_01 = "what did they say about regression in the third lecture?"

docs = vectordb.similarity_search(question, k=1)
print(docs)
vectordb.persist()

# print(len(md_chunks))
