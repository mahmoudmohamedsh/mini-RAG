from src.helpers.config import get_settings, Settings
from src.models import ResponseSignal
import os


class BaseController:

    def __init__(self):
        self.app_settings = get_settings()
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.files_dir = os.path.join(self.base_dir, "assets", "files")


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
