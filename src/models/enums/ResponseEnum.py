from enum import Enum


class ResponseSignal(Enum):
    FILE_TYPE_NOT_SUPPORTED = "File Type Not Supported"
    FILE_SIZE_EXCEEDED_10MB = "File size Exceed 10Mb"
    FILE_VALIDATE_SUCCESS = "File is Valide"
    FILE_UPLOAD_SUCCESS = "File Uploaded Successfully"
    FILE_UPLOAD_FAILD = "File Upload Faild"
    
    PROCESSING_FAILD="prcessing faild"
    PROCESSING_SUCCESS="prcessing success"