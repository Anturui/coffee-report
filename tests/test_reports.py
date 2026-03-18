import pytest
from coffee_report.reports.median_coffee import MedianCoffeeReport
from coffee_report.reports.registry import get_report, register_report
from coffee_report.reports.base import BaseReport

def test_median_calculation(sample_data):
    report = MedianCoffeeReport(sample_data)
    results = report.calculate()
    
    # Алексей: [100, 200] -> median 150
    # Иван: [300] -> median 300
    assert len(results) == 2
    assert results[0]['student'] == 'Иван'  # сортировка по убыванию
    assert results[0]['median_coffee'] == 300
    assert results[1]['median_coffee'] == 150

def test_registry():
    # Проверяем, что отчет зарегистрирован
    report = get_report('median-coffee', [])
    assert isinstance(report, MedianCoffeeReport)

def test_register_new_report():
    @register_report('test-report')
    class TestReport(BaseReport):
        @property
        def headers(self):
            return ['test']
        def calculate(self):
            return [{'test': 1}]
    
    report = get_report('test-report', [])
    assert report.calculate() == [{'test': 1}]