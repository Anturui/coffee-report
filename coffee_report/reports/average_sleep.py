import statistics
from collections import defaultdict
from typing import List, Dict, Any
from .base import BaseReport
from .registry import register_report

@register_report('average-sleep')
class AverageSleepReport(BaseReport):
    @property
    def headers(self) -> List[str]:
        return ["student", "avg_sleep"]
    
    def calculate(self) -> List[Dict[str, Any]]:
        sleeps = defaultdict(list)
        for row in self.data:
            sleeps[row['student']].append(row['sleep_hours'])
        
        results = [
            {'student': s, 'avg_sleep': round(statistics.mean(v), 1)}
            for s, v in sleeps.items()
        ]
        results.sort(key=lambda x: x['avg_sleep'], reverse=True)
        return results