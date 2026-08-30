from httpx import Response

from clients.api_client import ApiClient
from clients.api_courses.files.files_scheme import CreateFileRequestScheme
from clients.api_courses.private_http_builder import (
    get_private_http_client,
    AuthenticationScheme,
)


class FileClient(ApiClient):
    def create_file_api(self, request: CreateFileRequestScheme) -> Response:
        return self.client.post(
            url="/api/v1/files",
            data=request.model_dump(by_alias=True, exclude={"upload_file"}),
            files={"upload_file": open(request.upload_file, "rb")},
        )

    def delete_file_api(self, file_id: str) -> Response:
        return self.client.delete(url=f"/api/v1/files/{file_id}")

    def get_file_api(self, file_id: str) -> Response:
        return self.client.get(url=f"/api/v1/files/{file_id}")


def get_file_http_client(user: AuthenticationScheme) -> FileClient:
    return FileClient(get_private_http_client(user))
