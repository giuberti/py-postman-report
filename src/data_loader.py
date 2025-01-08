import json
from data_models import ReportData, TestResult

class JSONDataLoader:
    @staticmethod
    def load_data(file_path: str) -> ReportData:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        results = [TestResult(
            name=r['name'],
            url=r['url'],
            time=r['time'],
            all_tests=r['allTests']
        ) for r in data['results']]

        return ReportData(
            name=data['name'],
            timestamp=data['timestamp'],
            total_pass=data['totalPass'],
            total_fail=data['totalFail'],
            total_time=data['totalTime'],
            results=results
        )