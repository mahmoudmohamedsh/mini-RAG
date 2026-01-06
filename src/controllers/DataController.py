import os
import re
from src.models import ResponseSignal
from .BaseController import BaseController
from .ProjectController import ProjectController


class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576  # mb -> byte

    def validate_uploaded_file(self, file):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED

        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False,  ResponseSignal.FILE_SIZE_EXCEEDED_10MB

        return True,  ResponseSignal.FILE_VALIDATE_SUCCESS

    def generate_unique_file_name(self, original_file_name: str, project_id: str):

        random_string = self.generate_random_string()
        clean_file_name = self.get_clean_file_name(
            orig_file_name=original_file_name)

        project_file_dir = ProjectController().get_project_path(project_id=project_id)

        new_file_path = os.path.join(
            project_file_dir,
            random_string+"_"+clean_file_name
        )

        while os.path.exists(new_file_path):
            random_string = self.generate_random_string()
            new_file_path = os.path.join(
                project_file_dir,
                random_string+"_"+clean_file_name
            )
        file_id = random_string+"_"+clean_file_name
        return new_file_path, file_id

    def get_clean_file_name(self, orig_file_name: str):

        # remove any special characters, except underscore and .
        cleaned_file_name = re.sub(r'[^\w.]', '', orig_file_name.strip())

        # replace spaces with underscore
        cleaned_file_name = cleaned_file_name.replace(" ", "_")

        return cleaned_file_name
