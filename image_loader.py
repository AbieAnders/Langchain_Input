#Image
from langchain.document_loaders.image import UnstructuredImageLoader
def image_loader():
    loader = UnstructuredImageLoader("picture_name.file_extension", mode="elements")
    data = loader.load()
    print(data[0])