import pytest
from coffee_report.readers import read_csv_files

def test_read_csv(sample_csv):
    data = read_csv_files([sample_csv])
    assert len(data) == 3
    assert data[0]['student'] == 'Алексей Смирнов'
    assert data[0]['coffee_spent'] == 450  # проверка int конверсии

def test_read_nonexistent():
    with pytest.raises(FileNotFoundError):
        read_csv_files(['nonexistent.csv'])