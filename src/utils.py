import statistics
from typing import List
from data_models import TestResult

class TimeConverter:
    @staticmethod
    def ms_to_seconds_and_ms(milliseconds: int) -> str:
        seconds = milliseconds // 1000
        remaining_ms = milliseconds % 1000
        return f"{seconds}s {remaining_ms}ms"

class StatisticsCalculator:
    @staticmethod
    def calculate_average_time(data: List[TestResult], prop: str) -> float:
        time_values = [getattr(obj, prop) for obj in data]
        return round(statistics.mean(time_values) if time_values else 0, 1)