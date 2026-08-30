from httpx import Response

from clients.api_client import ApiClient
from clients.api_courses.courses.courses_scheme import (
    CreateCourseRequestScheme,
    UpdateCourseScheme,
)
from clients.api_courses.private_http_builder import (
    AuthenticationScheme,
    get_private_http_client,
)


class CourseClient(ApiClient):
    def create_course_api(self, request: CreateCourseRequestScheme) -> Response:
        return self.client.post(
            url="/api/v1/courses", json=request.model_dump(by_alias=True)
        )

    def get_courses_api(self, user_id: str) -> Response:
        return self.client.get(url="/api/v1/courses", params=user_id)

    def get_course_api(self, user_id: str) -> Response:
        return self.client.get(url=f"/api/v1/courses/{user_id}")

    def update_course_api(self, user_id: str, request: UpdateCourseScheme) -> Response:
        return self.client.patch(
            url=f"/api/v1/courses/{user_id}", json=request.model_dump(by_alias=True)
        )

    def delete_course_api(self, user_id: str) -> Response:
        return self.client.delete(url=f"/api/v1/courses/{user_id}")


def get_courses_http_client(user: AuthenticationScheme) -> CourseClient:
    return CourseClient(get_private_http_client(user=user))
