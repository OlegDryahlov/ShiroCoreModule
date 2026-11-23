"""Модуль ShiroCore."""

from utils.text import get_text


class Handler:
    """Модуль ShiroCore."""

    @property
    def button(self) -> str:
        """Текст кнопки модуля."""
        return get_text("ShiroCoreModule.button")

    def show(self) -> None:
        """Запуск модуля."""
        input(get_text("ShiroCoreModule.message"))
