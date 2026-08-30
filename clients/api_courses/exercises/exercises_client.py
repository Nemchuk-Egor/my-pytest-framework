from httpx import Response

from clients.api_client import ApiClient
from clients.api_courses.exercises.exercises_scheme import (
    CreateExerciseRequestScheme,
    UpdateExerciseRequestScheme,
)
from clients.api_courses.private_http_builder import (
    AuthenticationScheme,
    get_private_http_client,
)


class ExerciseClient(ApiClient):
    def create_exercise_api(self, request: CreateExerciseRequestScheme) -> Response:
        return self.client.post(
            url="/api/v1/exercises", json=request.model_dump(by_alias=True)
        )

    def get_exercises_api(self) -> Response:
        return self.client.get(url="/api/v1/exercises")

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.client.get(url=f"/api/v1/exercises/{exercise_id}")

    def update_exercise_api(
        self, exercise_id: str, request: UpdateExerciseRequestScheme
    ) -> Response:
        return self.client.patch(
            url=f"/api/v1/exercises/{exercise_id}",
            json=request.model_dump(by_alias=True),
        )

    def delete_exercise_api(self, exercise_id) -> Response:
        return self.client.delete(url=f"/api/v1/exercises/{exercise_id}")


def create_http_exercise_client(user: AuthenticationScheme) -> ExerciseClient:
    return ExerciseClient(get_private_http_client(user))
