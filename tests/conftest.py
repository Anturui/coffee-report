import pytest
import tempfile
import os

@pytest.fixture
def sample_csv():
    """Фикстура с тестовыми данными."""
    content = """student,date,coffee_spent,sleep_hours,study_hours,mood,exam
Алексей Смирнов,2024-06-01,450,4.5,12,норм,Математика
Алексей Смирнов,2024-06-02,500,4.0,14,устал,Математика
Иван Кузнецов,2024-06-01,600,3.0,15,зомби,Математика"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8') as f:
        f.write(content)
        f.flush()
        yield f.name
    
    os.unlink(f.name)

@pytest.fixture
def sample_data():
    """Готовые данные без чтения файла."""
    return [
        {'student': 'Алексей', 'coffee_spent': 100, 'date': '2024-01-01', 'exam': 'Math'},
        {'student': 'Алексей', 'coffee_spent': 200, 'date': '2024-01-02', 'exam': 'Math'},
        {'student': 'Иван', 'coffee_spent': 300, 'date': '2024-01-01', 'exam': 'Math'},
    ]