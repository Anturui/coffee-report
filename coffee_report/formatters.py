from typing import List, Dict, Any
from tabulate import tabulate

def format_table(data: List[Dict[str, Any]], headers: List[str]) -> str:
    """Форматирует данные в таблицу для консоли."""
    if not data:
        return "Нет данных"
    
    # Конвертируем словари в списки по порядку headers
    table_data = [[row.get(h, '') for h in headers] for row in data]
    
    return tabulate(
        table_data, 
        headers=headers, 
        tablefmt='grid', 
        colalign=['left', 'right']
    )