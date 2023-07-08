import os
import openai
from dotenv import load_dotenv

# import PyPDFLoader from langchain
from langchain.document_loaders import PyPDFLoader

# import autoloader from langchain
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser

# import WebBasedLoader from langchain
from langchain.document_loaders.web_base import WebBaseLoader

# import data from Notion
from langchain.document_loaders import NotionDBLoader

# load the .env file
load_dotenv()

# reference
PDF_File = r"C:\Users\ROG\Downloads\1-s2.0-S0926580515000370-main.pdf"
Notion_DB = "https://www.notion.so/a11ab2438d224563a4997fd73ed15f97?v=eed6f674983f43fd98c478e9a3db5ac5&pvs=4"
Youtube_url = "https://www.youtube.com/watch?v=KwAXfey-xQk"
Page_URL = "https://python.langchain.com/docs/get_started/introduction"
Save_dir = r"C:\Users\ROG\Downloads\langchain_test"

# get the api key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# get notion token and database id
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")


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

# load the notion database
notion_loader = NotionDBLoader(
    integration_token=NOTION_TOKEN,
    database_id=DATABASE_ID,
    request_timeout_sec=30,  # optional, defaults to 10
)
notion_pages = notion_loader.load()
print(notion_pages)