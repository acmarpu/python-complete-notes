"""
Problem Statement: Create a Python script that automates the process of creating a new issue in JIRA using the JIRA REST API.
The script should take user input for the issue details such as project key, issue type, summary, 
and description, and then use this information to create a new issue in JIRA

"""

# Codeing Template

# 1. import the required modules

import os
import requests     # Make API calls over the web (GET, POST, PUT, DELETE)
import re
from dotenv import load_dotenv
from jira import JIRA


# 2. input variables

# Initialization 
# load environment variables from .env file

load_dotenv()
JIRA_URL = os.getenv("JIRA_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
PROJECT_KEY = os.getenv("PROJECT_KEY")

# Connecting to JIRA
jira = JIRA(server=JIRA_URL, basic_auth=(JIRA_USERNAME, JIRA_API_TOKEN))


# 3. constants
issue_type = 'Task'  # Default issue type, can be modified as needed


# 4. Define each and every stages of the process as a function
def create_issue(summary, description):
    # create a new issue in JIRA
    issue_dict = {
        'project': {'key': PROJECT_KEY},
        'summary': summary,
        'description': description,
        'issuetype': {'name': issue_type},
    }
    try:
        new_issue = jira.create_issue(fields=issue_dict)
        print(f"Issue {new_issue.key} created successfully.")
        
    except Exception as e:
        print(f"Error creating issue: {e}")
       


# 5. main  block
def main():
    # Input details
    summary = input("Enter the issue summary: ")
    description = input("Enter the issue description: ")
    # Call Create Issue function
    create_issue(summary, description)
    

if __name__ == "__main__":
    main()
    

