from abc import ABC, abstractmethod
from typing import List
from data_models import ReportData, TestResult
from formatters import ResultFormatter
from utils import TimeConverter, StatisticsCalculator

class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, data: ReportData) -> str:
        pass

class HTMLReportGenerator(ReportGenerator):
    def __init__(self, result_formatter: ResultFormatter):
        self.result_formatter = result_formatter

    def generate_report(self, data: ReportData) -> str:
        template = self._get_html_template()
        content = template.replace("--TIMESTAMP--", data.timestamp)
        content = content.replace("--NAME--", data.name)
        content = content.replace("--PASSED--", str(data.total_pass))
        content = content.replace("--QTY--", str(len(data.results)))
        content = content.replace("--TOTAL TIME--", TimeConverter.ms_to_seconds_and_ms(data.total_time))
        content = content.replace("--AVG TIME--", str(StatisticsCalculator.calculate_average_time(data.results, "time")))
        content = content.replace("--FAILED--", str(data.total_fail))
        content = content.replace("--XPTO--", self._draw_results(data.results))
        return content

    def _draw_results(self, results: List[TestResult]) -> str:
        return "".join(self.result_formatter.format_result(result) for result in results)

    def _get_html_template(self) -> str:
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            <title>--NAME--</title>
            <style>               
                .list-group-item {
                    border-left: 0px none;
                    border-top: 0px none;
                    border-bottom: 1px solid #cdcdcd;
                    border-right: 0px none;
                }
            </style>
        </head>
        <body>
            <div class='container'>
            <h4>--NAME--</h4>
            <h6>--TIMESTAMP--</h6>
            <header class="d-flex flex-wrap justify-content-between align-items-left py-3 my-4 border-bottom">
                <div class="col-md-8 d-flex align-items-left">
                    <div class="row text-left">
                        <div class="col">
                            <span class="text-body-primary d-block"><small>Duration</small></span>
                            <span class="text-body-secondary">--TOTAL TIME--</span>
                        </div>
                        <div class="col">
                            <span class="text-body-primary d-block"><small>Scenarios</small></span>
                            <span class="text-body-secondary">--QTY--</span>
                        </div>
                        <div class="col">
                            <span class="text-body-primary d-block"><small>Avg Response</small></span>
                            <span class="text-body-secondary">--AVG TIME-- ms</span>
                        </div>
                    </div>
                </div>
                <ul class="nav col-md-4 justify-content-end">
                    <li class="nav-item"><span class="badge text-bg-success">--PASSED-- Passed</li>
                    <li class="nav-item"><span class="badge text-bg-danger">--FAILED-- Failed</li>
                </ul>
            </header>
                <div class="list-group">
                --XPTO--
                </div>
            </div>
        </body>
        </html>
        """