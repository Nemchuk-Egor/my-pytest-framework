from pydantic import BaseModel, Field


class FileScheme(BaseModel):
    id: str
    filename: str
    directory: str
    url: str


class CreateFileRequestScheme(BaseModel):
    filename: str
    directory: str
    upload_file: str


class CreateFileResponseScheme(BaseModel):
    file: FileScheme


class GetFileResponseScheme(BaseModel):
    file: FileScheme
