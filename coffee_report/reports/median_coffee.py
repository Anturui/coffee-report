import statistics
from collections import defaultdict
from typing import List, Dict, Any
from .base import BaseReport
from .registry import register_report

@register_report('median-coffee')
class MedianCoffeeReport(BaseReport):
    """Отчет: медианные траты на кофе по студентам."""
    
    @property
    def headers(self) -> List[str]:
        return ["student", "median_coffee"]
    
    def calculate(self) -> List[Dict[str, Any]]:
        spends: Dict[str, List[int]] = defaultdict(list)
        
        for row in self.data:
            spends[row['student']].append(row['coffee_spent'])
        
        results = []
        for student, values in spends.items():
            results.append({
                'student': student,
                'median_coffee': int(statistics.median(values))
            })
        
        results.sort(key=lambda x: x['median_coffee'], reverse=True)
        return results