"""Приватный клиент для работы с пользователями.

Модуль содержит класс :class:`PrivateUserClient` — клиент эндпоинтов
пользователей, требующих авторизации, а также фабричную функцию
:func:`get_private_user_client`, которая создаёт авторизованный
HTTP-клиент на основе данных пользователя.
"""

from client.api_client import ApiClient
from httpx import Response

from client.private_http_builder import AuthenticationSchema, get_private_http_client
from client.user.user_schema import UpdateUserRequestSchema


class PrivateUserClient(ApiClient):
    """Клиент приватных эндпоинтов пользователей.

    Наследует базовые HTTP-методы от :class:`ApiClient` и добавляет
    методы для сценариев работы с текущим и произвольным пользователем.
    """

    def get_user_me_api(self) -> Response:
        """Запрашивает данные текущего аутентифицированного пользователя.

        :return: объект ответа httpx.
        """
        return self.client.get(url="/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """Запрашивает данные пользователя по идентификатору.

        :param user_id: идентификатор пользователя.
        :return: объект ответа httpx.
        """
        return self.client.get(url=f"/api/v1/users/{user_id}")

    def update_user_api(
        self, request: UpdateUserRequestSchema, user_id: str
    ) -> Response:
        """Обновляет данные пользователя по идентификатору.

        Незаполненные (``None``) поля запроса не отправляются — это
        позволяет частично обновлять пользователя.

        :param request: поля пользователя для обновления.
        :param user_id: идентификатор пользователя.
        :return: объект ответа httpx.
        """
        return self.client.patch(
            url=f"/api/v1/users/{user_id}",
            json=request.model_dump(by_alias=True, exclude_none=True),
        )

    def delete_api(self, user_id: str) -> Response:
        """Удаляет пользователя по идентификатору.

        :param user_id: идентификатор пользователя.
        :return: объект ответа httpx.
        """
        return self.client.delete(url=f"/api/v1/users/{user_id}")


def get_private_user_client(user: AuthenticationSchema) -> PrivateUserClient:
    """Создаёт приватный клиент пользователя.

    :param user: учётные данные пользователя для авторизации.
    :return: экземпляр :class:`PrivateUserClient` с авторизованным
        HTTP-клиентом.
    """
    return PrivateUserClient(get_private_http_client(user))
