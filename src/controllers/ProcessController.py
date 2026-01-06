from .BaseController import BaseController
from .ProjectController import ProjectController
import os
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.models import PrcessingEnum


class ProcessController(BaseController):
    def __init__(self, project_id: str):
        super().__init__()
        self.project_id = project_id
        self.project_folder_path = ProjectController(
        ).get_project_path(project_id=project_id)

    def get_file_extention(self, file_id: str):
        return os.path.splitext(file_id)[-1]

    def get_file_loader(self, file_id: str):

        file_extention = self.get_file_extention(file_id=file_id)
        file_path: str = os.path.join(self.project_folder_path, file_id)

        if file_extention == PrcessingEnum.TXT.value:
            return TextLoader(file_path=file_path, encoding="utf-8")
        elif file_extention == PrcessingEnum.PDF.value:
            return PyMuPDFLoader(file_path=file_path)
        else:
            return None

    def get_file_content(self, file_id: str):
        loader = self.get_file_loader(
            file_id=file_id
        )

        return loader.load()  # [ Document( file_content , metadata )]

    def process_file_content(self, file_content: list, chunk_size: int = 100, overlap_size: int = 20):
        text_spliter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap_size,
            lenght_function=len
        )

        file_context_texts = [record.page_content for record in file_content]
        file_context_metadata = [record.metadata for record in file_content]

        chunks = text_spliter.create_documents(
            file_context_texts,
            metadatas=file_context_metadata
        )

        return chunks
