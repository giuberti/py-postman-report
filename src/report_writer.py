class ReportWriter:
    @staticmethod
    def write_report(content: str, file_path: str):
        with open(file_path, 'w') as file:
            file.write(content)
