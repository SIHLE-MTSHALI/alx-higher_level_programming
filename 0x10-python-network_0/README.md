# Python Network Project #0

This project is designed to help you understand various networking concepts with Bash and Python. The tasks involve sending HTTP requests, handling responses, and exploring different HTTP methods using `cURL`. You will also create Python scripts to find a peak in a list of unsorted integers. Below is a breakdown of the tasks and files in this project, along with their explanations.

## Directory Structure
The following directories and files are part of this project:

- `0x10-python-network_0/`: Root directory for the project.

## Project Files and Tasks

### Task 0: cURL Body Size
- **File**: `0-body_size.sh`
- **Description**: A Bash script that sends a request to a specified URL and displays the size of the body of the response in bytes.
- **Command to Run**: `./0-body_size.sh <URL>`
- **How It Works**: The script uses `cURL` with the `-s` option (silent mode), pipes the output to `wc -c` to count the characters (bytes), and displays the result.

### Task 1: cURL to the End
- **File**: `1-body.sh`
- **Description**: A Bash script that sends a GET request to a specified URL and displays the body of the response, but only for HTTP status code 200.
- **Command to Run**: `./1-body.sh <URL>`
- **How It Works**: The script uses `cURL` with the `-s` (silent) and `-L` (follow redirects) options to get the body of the response.

### Task 2: cURL Method
- **File**: `2-delete.sh`
- **Description**: A Bash script that sends a DELETE request to a specified URL and displays the body of the response.
- **Command to Run**: `./2-delete.sh <URL>`
- **How It Works**: The script uses `cURL` with the `-sX DELETE` options to send a DELETE request.

### Task 3: cURL Only Methods
- **File**: `3-methods.sh`
- **Description**: A Bash script that retrieves all HTTP methods a server will accept and displays them.
- **Command to Run**: `./3-methods.sh <URL>`
- **How It Works**: The script uses `cURL` with the `-sI` options to fetch the headers, then `grep` to find the "Allow" header, and `cut` to extract the list of allowed methods.

### Task 4: cURL Headers
- **File**: `4-header.sh`
- **Description**: A Bash script that sends a GET request with a custom header to a specified URL and displays the body of the response.
- **Command to Run**: `./4-header.sh <URL>`
- **How It Works**: The script uses `cURL` with the `-s` option and a custom header (`X-School-User-Id: 98`) to send the GET request.

### Task 5: cURL POST Parameters
- **File**: `5-post_params.sh`
- **Description**: A Bash script that sends a POST request with specific parameters to a specified URL and displays the body of the response.
- **Command to Run**: `./5-post_params.sh <URL>`
- **How It Works**: The script uses `cURL` with the `-s` option, sends POST data with the `-d` flag (containing email and subject), and displays the body of the response.

### Task 6: Find a Peak
- **Files**: `6-peak.py`, `6-main.py`, `6-peak.txt`
- **Description**: Python code to find a peak in a list of unsorted integers.
- **Commands to Run**: `./6-main.py`
- **How It Works**: The script `6-peak.py` contains the `find_peak` function, which uses a binary search approach to find a peak with a time complexity of O(log(n)). The test script `6-main.py` checks the function's output with various inputs. The text file `6-peak.txt` explains the algorithm's complexity.

### Task 7: Only Status Code
- **File**: `100-status_code.sh`
- **Description**: A Bash script that sends a request to a specified URL and displays only the HTTP status code of the response.
- **Command to Run**: `./100-status_code.sh <URL>`
- **How It Works**: The script uses `cURL` with the `-s`, `-o /dev/null` (to ignore output), and `-w "%{http_code}"` to display only the HTTP status code.

### Task 8: cURL a JSON File
- **File**: `101-post_json.sh`
- **Description**: A Bash script that sends a POST request with a JSON file in the body to a specified URL and displays the response.
- **Command to Run**: `./101-post_json.sh <URL> <filename>`
- **How It Works**: The script uses `cURL` with the `-s`, `-X POST`, and `-H "Content-Type: application/json"` options to send a POST request with a JSON file as the request body.

### Task 9: Catch Me If You Can
- **File**: `102-catch_me.sh`
- **Description**: A Bash script that sends a request to `0.0.0.0:5000/catch_me` that results in a response containing "You got me!".
- **Command to Run**: `./102-catch_me.sh`
- **How It Works**: The script uses `cURL` with the `-s`, `-X PUT`, `-L` (follow redirects), and a custom header, along with data to trigger the expected response from the server.

## Usage
To run each script, ensure they are executable and provide the necessary arguments, if required. Test each script using the provided commands to verify the expected output.

