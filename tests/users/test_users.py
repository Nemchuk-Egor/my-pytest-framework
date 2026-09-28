"""Тесты API пользователей.

Покрывают создание, получение, обновление и удаление пользователя,
а также проверку JSON Schema ответов и сценарий с невалидным токеном
после удаления.
"""

from http import HTTPStatus

import pytest

from client.errors_schema import InternalErrorsResponseSchema
from client.user.private_user_client import PrivateUserClient
from client.user.public_user_client import PublicUserClient
from client.user.user_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    GetUserResponseSchema,
    UpdateUserRequestSchema,
    UpdateUserResponseSchema,
)
from fixtures.users import UserFixtures, private_user_client
from tools.assertion.errors import assert_invalid_or_expired_token
from tools.fake import fake
from tools.assertion.base import assert_status_code
from tools.assertion.user import (
    assert_create_user_response,
    assert_get_user_response,
    assert_update_user_response,
)
from tools.assertion.json_schema import validation_json_schema


@pytest.mark.user
@pytest.mark.regression
class TestUser:
    """Набор регрессионных тестов для эндпоинтов пользователей."""

    @pytest.mark.parametrize("domain", ["gmail.com", "example.com", "yandex.ru"])
    def test_create_user(self, public_user_client: PublicUserClient, domain: str):
        """Создание пользователя с email на разных доменах.

        Проверяет статус 200, соответствие ответа запросу и JSON Schema.
        """
        email = fake.email(domain=domain)
        request = CreateUserRequestSchema(email=email)
        response = public_user_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(response_data, request)

        validation_json_schema(response.json(), response_data.model_json_schema())

    def test_get_user(
        self, function_user: UserFixtures, private_user_client: PrivateUserClient
    ):
        """Получение пользователя по id авторизованным клиентом.

        Проверяет статус 200, совпадение с данными при создании
        и JSON Schema.
        """
        response = private_user_client.get_user_api(function_user.response.user.id)
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_user.response)

        validation_json_schema(response.json(), response_data.model_json_schema())

    def test_get_user_me(
        self, function_user: UserFixtures, private_user_client: PrivateUserClient
    ):
        """Получение текущего пользователя через ``/users/me``.

        Проверяет статус 200, совпадение с данными при создании
        и JSON Schema.
        """
        response = private_user_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_user.response)

        validation_json_schema(response.json(), response_data.model_json_schema())

    @pytest.mark.parametrize(
        "update_user_request",
        [
            pytest.param(
                lambda f: UpdateUserRequestSchema(email=fake.email()), id="only_email"
            ),
            pytest.param(
                lambda f: UpdateUserRequestSchema(
                    email=fake.email(),
                    last_name=fake.last_name(),
                    first_name=fake.first_name(),
                    middle_name=fake.middle_name(),
                ),
                id="all_fields",
            ),
        ],
        indirect=True,
    )
    def test_update_user(
        self,
        function_user: UserFixtures,
        private_user_client: PrivateUserClient,
        update_user_request: UpdateUserRequestSchema,
    ):
        """Обновление пользователя: только email или все поля.

        Проверяет статус 200, соответствие ответа запросу и JSON Schema.
        """
        response = private_user_client.update_user_api(
            update_user_request, function_user.response.user.id
        )
        response_data = UpdateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_user_response(response_data, update_user_request)

        validation_json_schema(response.json(), response_data.model_json_schema())

    def test_delete_user(
        self,
        function_user: UserFixtures,
        private_user_client: PrivateUserClient,
    ):
        """Удаление пользователя и проверка, что токен больше не действует.

        После удаления повторный GET должен вернуть 401 и сообщение
        ``Invalid or expired token``.
        """
        response = private_user_client.delete_api(function_user.response.user.id)

        assert_status_code(response.status_code, HTTPStatus.OK)

        get_user_response = private_user_client.get_user_api(
            function_user.response.user.id
        )
        get_user_response_data = InternalErrorsResponseSchema.model_validate_json(
            get_user_response.text
        )

        assert_status_code(get_user_response.status_code, HTTPStatus.UNAUTHORIZED)
        assert_invalid_or_expired_token(get_user_response_data)
