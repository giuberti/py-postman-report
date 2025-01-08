from data_loader import JSONDataLoader
from report_generators import HTMLReportGenerator
from formatters import HTMLResultFormatter # type: ignore
from report_writer import ReportWriter

def main():
    # Constants (consider moving these to a separate configuration file)
    PATH_INPUT_RESULTS = 'path/to/input/results.json'
    PATH_OUTPUT_REPORT = 'path/to/output/report.html'

    # Load data
    data = JSONDataLoader.load_data(PATH_INPUT_RESULTS)

    # Generate report
    report_generator = HTMLReportGenerator(HTMLResultFormatter())
    html_content = report_generator.generate_report(data)

    # Write report
    ReportWriter.write_report(html_content, PATH_OUTPUT_REPORT)

    print("HTML file has been generated successfully.")

if __name__ == "__main__":
    main()