from enum import Enum


class ResponseSignal(Enum):
    FILE_TYPE_NOT_SUPPORTED = ""
    FILE_SIZE_EXCEEDED_10MB = ""
    FILE_VALIDATE_SUCCESS = ""
    FILE_UPLOAD_SUCCESS = ""
    FILE_UPLOAD_FAILD = ""
