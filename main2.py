import json
from config.config import PATH_INPUT_RESULTS, PATH_OUTPUT_REPORT
import statistics
from src.logger import logger 

def calculate_average_time(data, prop):
    # Extract the time values from each object
    time_values = [obj[prop] for obj in data]    
    # Calculate the average time
    average_time = statistics.mean(time_values) if time_values else 0
    average_time = round(average_time, 1)
    return average_time

def ms_to_seconds_and_ms(milliseconds):
    seconds = milliseconds // 1000
    remaining_ms = milliseconds % 1000
    return f"{seconds}s {remaining_ms}ms"

def print_result(result):
    
    output = "<a href='#' class='list-group-item list-group-item-action d-flex gap-3 py-3' aria-current='true'>"
    output += "<div class='d-flex gap-2 w-100 justify-content-between'><div>"
    output += f"<h6 class='mb-0'>{result.get('name')}</h6>"
    output += f"<p class='mb-0 opacity-50'><small>{result.get('url')}</small></p>"

    for test in result["allTests"]:
        for test_name, value in test.items():
            color_class = "text-bg-success" if value else "text-bg-danger"
            output += f"<p class='mb-0 opacity-75'><span class='badge {color_class}'>&nbsp;</span> {test_name}</p>"

    output += "</div>"

    output += f"<small class='opacity-50 text-nowrap'>{result['time']} ms</small></div>"
   
    #output += f"<li class='list-group-item'>{printFamily(family)} {printCode(code, obj.get('trafficLight'))} {printJobProfile(jobProfile)} {printTrainningReq(trainningReq)} <span class='fw-light'>{result["name"]}</span>"

    output += "</a>\n"
    return output


def draw_results(data):
    output = ""
    results = data["results"]
    for result in results:
        output += print_result(result)
    return output


def generate_html(json_data):
    template_str = """
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
    
    content = template_str.replace("--TIMESTAMP--", json_data["timestamp"])
    content = content.replace("--NAME--", json_data["name"])
    content = content.replace("--PASSED--", str(json_data["totalPass"]))
    content = content.replace("--QTY--", str(len(json_data["results"])))
    content = content.replace("--TOTAL TIME--", ms_to_seconds_and_ms(json_data["totalTime"]))
    content = content.replace("--AVG TIME--", str(calculate_average_time(json_data["results"], "time")))
    content = content.replace("--FAILED--", str(json_data["totalFail"]))
    content = content.replace("--XPTO--", draw_results(json_data))



    return content

logger.log_info("Iniciando...")
# Read JSON data from a file
with open(PATH_INPUT_RESULTS, 'r') as file:
    json_data = json.load(file)

# Generate HTML content
html_content = generate_html(json_data)

# Write HTML content to a file
with open(PATH_OUTPUT_REPORT, 'w') as file:
    file.write(html_content)

print("HTML file has been generated successfully.")
