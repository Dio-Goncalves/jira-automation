# Jira Service Management Onboarding Automation

## Overview

This project showcases how to automate onboarding requests using Jira Cloud Rest API and Python. The employee information is automatically read from a CSV file and used to automatically create onboarding requests with populated custom fields such as:  

 - Employee first name;  
 - Employee last name;  
 - Company email;  
 - Department;  
 - Manager.  

The project also includes discovery scripts used to inspect Jira Cloud metadata, in order to better understand request types, custom fields and available options, before assembling the code.  

## Features

 - Authenticate with Jira Cloud REST API;  
 - Create Jira Service Management requests;  
 - Read employee data from CSV files;  
 - Populate Jira custom fields;  
 - Discover issue types, request types and request fields;  
 - Modular Python project structure

## Technologies

 - Python 3;  
 - Jira Cloud REST API;  
 - Jira Service Management;  
 - Git. 

## Project Structure

```
|-- data  
|   `-- employees.csv  
|-- jira_training  
|   |-- config.py  
|   |-- csv_reader.py  
|   |-- discovery  
|   |   |-- __init__.py  
|   |   |-- issue_types.py  
|   |   |-- project.py  
|   |   |-- request_fields.py  
|   |   |-- request_types.py  
|   |   |-- service_desk.py  
|   |   `-- user_fields.py  
|   |-- __init__.py  
|   |-- jira_client.py  
|   |-- main.py  
|   |-- onboarding_service.py  
|   `-- utilities  
|       |-- auth_test.py  
|       `-- __init__.py  
|-- README.md  
|-- requirements.txt  
`-- tests  
    |-- create_issue.py  
    |-- create_request.py  
    `-- test.py  
```

## Installation

**Clone the repository**  

```
git clone <repository-url>
```

**Create a virutal environment**

```
python3 -m venv .venv
```

**Activate it**  

Linux/macOS

```
source .venv/bin/activate
```

Windows

```
.venv/Scripts/activate
```

**Install dependencies** 

```
pip install -r requirements.txt
```

## Configuration

Directly change the variables on the `config.py` or you can go for a cleaner approach and use environment variables.  
The `config.py` file is already prepared to be used with environment variables, so you can just proceed with creating these and leave the `config.py` file untouched.  
The variables must contain:  
```
JIRA_URL = "https://your-domain.atlassian.net"
JIRA_EMAIL = "your-email@email.com"
JIRA_API_TOKEN = "your-api-token"
```

## Usage examples

**Run the main script**

```
python3 -m jira_training.main
```

**Discover available request fields**

```
python3 -m jira_training.discovery.request_fields
```

**Discover request types**

```
python3 -m jira_training.discovery.request_types
```

## Lessons Learned

During this project I learned:  
 - Jira Cloud REST API authentication;  
 - Working with Service Management request endpoints;  
 - Discovering Jira metadata dynamically;  
 - Handling different Jira field types;  
 - Building reusable API clients in Python;
 - Organizing a Python project into reusable modules.  

 ## Future Improvements

 - Child request creation;  
 - Logging. 
