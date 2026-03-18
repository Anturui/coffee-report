from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseReport(ABC):
    """Базовый класс для всех отчетов."""
    
    def __init__(self, data: List[Dict[str, Any]]):
        self.data = data
    
    @abstractmethod
    def calculate(self) -> List[Dict[str, Any]]:
        """Возвращает данные для таблицы."""
        pass
    
    @property
    @abstractmethod
    def headers(self) -> List[str]:
        """Заголовки колонок."""
        pass