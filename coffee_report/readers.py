import csv
from typing import List, Dict, Any
from pathlib import Path

def read_csv_files(file_paths: List[str]) -> List[Dict[str, Any]]:
    """
    Читает CSV файлы. Использует только модуль csv (стандартная библиотека).
    """
    all_data: List[Dict[str, Any]] = []
    
    for path_str in file_paths:
        path = Path(path_str)
        if not path.exists():
            raise FileNotFoundError(f"Файл не найден: {path}")
            
        with open(path, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                all_data.append({
                    'student': row['student'],
                    'date': row['date'],
                    'coffee_spent': int(row['coffee_spent']),
                    'sleep_hours': float(row['sleep_hours']),
                    'study_hours': int(row['study_hours']),
                    'mood': row['mood'],
                    'exam': row['exam']
                })
    
    return all_data