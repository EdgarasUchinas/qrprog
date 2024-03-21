import os

class Config:
    QR_CODE_IMAGE_DIRECTORY = os.environ.get("QR_CODE_IMAGE_DIRECTORY")
    QR_CODE_IMAGE_FILE_NAME = os.environ.get("QR_CODE_DEFAULT_FILE_NAME")
    QR_CODE_DEFAULT_URL = os.environ.get("QR_CODE_DEFAULT_URL")