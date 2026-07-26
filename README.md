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
 - Git;  
 - Bitbucket.  

## Project Structure

```text
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

