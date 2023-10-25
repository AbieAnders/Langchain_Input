#import langchain
#print(langchain.__file__)

#Pdf
from langchain.document_loaders import PyPDFLoader
def pdf_loader():
    loader = PyPDFLoader("example_data/layout-parser-paper.pdf")
    pages = loader.load_and_split()
    print(pages[0])