# Nux Python Client

## Overview
The Nux Python Client is a simple and effective way to interact with the Nux API. It simplifies the process of making requests to Nux API services, handling authentication, and processing responses.

## Features
- Easy to use interface for interacting with Nux API.
- Supports running workbooks with custom parameters.
- Handles API authentication seamlessly.

## Installation
To install the Nux Python Client, simply use pip:

```shell
pip install nuxai
```

## Usage

### Setting Up

```python
from nuxai import NuxAI

api_key = 'your_api_key_here'
nux_client = NuxAI(api_key)
```

### Running a Workbook
To run a workbook with the client:

```python
workbook_id = 'your_workbook_id'
parameters = {
    # Your parameters here
}

response = nux_client.run(workbook_id, parameters)

if response:
    print(response)
else:
    print("Failed to run the workbook")
```

## Handling Errors
The client provides basic error handling, displaying the HTTP status code and response text in case of an error.