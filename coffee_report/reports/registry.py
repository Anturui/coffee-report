from typing import Dict, Type, List, Any
from .base import BaseReport

_report_registry: Dict[str, Type[BaseReport]] = {}

def register_report(name: str):
    """
    Декоратор для регистрации новых отчетов.
    Использование: @register_report('median-coffee')
    """
    def decorator(cls: Type[BaseReport]) -> Type[BaseReport]:
        if not issubclass(cls, BaseReport):
            raise TypeError(f"Класс {cls} должен наследовать BaseReport")
        _report_registry[name] = cls
        return cls
    return decorator

def get_report(name: str, data: List[Dict[str, Any]]) -> BaseReport:
    """Фабрика отчетов."""
    if name not in _report_registry:
        available = ", ".join(_report_registry.keys())
        raise ValueError(f"Отчет '{name}' не найден. Доступные: {available}")
    return _report_registry[name](data)

def list_reports() -> list:
    """Возвращает список доступных отчетов."""
    return list(_report_registry.keys())