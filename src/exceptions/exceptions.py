class ValidationError(TypeError):
    """Ошибка валидации."""


class APIConnectionError(ConnectionError):
    """Ошибка подключения к API."""


class CountryNotFoundError(ValueError):
    """Страна не найдена."""
