from fastapi_storages import FileSystemStorage, S3Storage

from api.src.settings import settings


class MainS3Storage(S3Storage):
    AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY
    AWS_S3_BUCKET_NAME = settings.AWS_S3_BUCKET_NAME
    AWS_S3_ENDPOINT_URL = settings.AWS_S3_ENDPOINT_URL
    AWS_S3_USE_SSL = settings.AWS_S3_USE_SSL
    AWS_DEFAULT_ACL = settings.AWS_DEFAULT_ACL
    AWS_QUERYSTRING_AUTH = settings.AWS_QUERYSTRING_AUTH
    AWS_S3_CUSTOM_DOMAIN = settings.AWS_S3_CUSTOM_DOMAIN


file_storage = None
if settings.DEBUG:
    file_storage = FileSystemStorage("./files")
else:
    file_storage = MainS3Storage()
