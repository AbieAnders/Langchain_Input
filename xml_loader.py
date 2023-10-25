#Xml
from langchain.document_loaders import UnstructuredXMLLoader
def xml_loader():
    loader = UnstructuredXMLLoader(
        "example_data/file_name.xml",
    )
    docs = loader.load()
    print(docs[0])
