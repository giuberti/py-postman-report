from abc import ABC, abstractmethod
from data_models import TestResult

class ResultFormatter(ABC):
    @abstractmethod
    def format_result(self, result: TestResult) -> str:
        pass

class HTMLResultFormatter(ResultFormatter):
    def format_result(self, result: TestResult) -> str:
        output = "<a href='#' class='list-group-item list-group-item-action d-flex gap-3 py-3' aria-current='true'>"
        output += "<div class='d-flex gap-2 w-100 justify-content-between'><div>"
        output += f"<h6 class='mb-0'>{result.name}</h6>"
        output += f"<p class='mb-0 opacity-50'><small>{result.url}</small></p>"

        for test in result.all_tests:
            for test_name, value in test.items():
                color_class = "text-bg-success" if value else "text-bg-danger"
                output += f"<p class='mb-0 opacity-75'><span class='badge {color_class}'>&nbsp;</span> {test_name}</p>"

        output += "</div>"
        output += f"<small class='opacity-50 text-nowrap'>{result.time} ms</small></div>"
        output += "</a>\n"
        return output