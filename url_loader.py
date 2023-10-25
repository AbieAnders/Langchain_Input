#Url
from langchain.document_loaders import UnstructuredURLLoader
def url_loader():
    my_urls = [
        "URL of choice 1",
        "URL of choice 2",
    ]
    loader = UnstructuredURLLoader(urls=my_urls)
    data = loader.load()
    print(data[0])