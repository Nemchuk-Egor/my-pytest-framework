"""Генератор тестовых данных на основе ``Faker``.

Модуль предоставляет класс :class:`Fake` — обёртку над ``Faker``
с фиксированной локалью ``ru_RU`` и удобными методами для генерации
данных, используемых в тестах, а также готовый экземпляр ``fake``.
"""

from faker import Faker


class Fake:
    """Обёртка над ``Faker`` для генерации тестовых данных.

    Инкапсулирует конкретный экземпляр ``Faker`` и предоставляет
    типизированные методы для часто используемых полей.
    """

    def __init__(self, faker: Faker) -> None:
        """Инициализирует обёртку.

        :param faker: настроенный экземпляр ``Faker``.
        """
        self.faker = faker

    def uuid4(self) -> str:
        """Генерирует случайный UUID4.

        :return: строковое представление UUID4.
        """
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """Генерирует случайный email.

        :param domain: домен для адреса; если не задан — выбирается
            случайно.
        :return: email-адрес.
        """
        return self.faker.email(domain=domain)

    def password(self) -> str:
        """Генерирует случайный пароль.

        :return: строка пароля.
        """
        return self.faker.password()

    def last_name(self) -> str:
        """Генерирует случайную фамилию.

        :return: фамилия.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """Генерирует случайное имя.

        :return: имя.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """Генерирует случайное отчество.

        :return: отчество.
        """
        return self.faker.middle_name()


# Готовый экземпляр для использования как зависимость/синглтон.
fake = Fake(Faker("ru_RU"))
