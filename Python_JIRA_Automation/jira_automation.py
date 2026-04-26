"""
Problem Statement: Create a Python script that automates the process of creating a new issue in JIRA using the JIRA REST API.
The script should take user input for the issue details such as project key, issue type, summary, 
and description, and then use this information to create a new issue in JIRA

"""

# Codeing Template

# 1. import the required modules

import os
#import requests
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

# define each and v=every stages of the process as a function
def create_issue(summary, description, assignee):
    # create a new issue in JIRA
    issue_dict = {
        'project': {'key': PROJECT_KEY},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Task'},
        'assignee': {'name': assignee},
    }
    try:
        new_issue = jira.create_issue(fields=issue_dict)
        print(f"Issue {new_issue.key} created successfully.")
    except Exception as e:
        print(f"Error creating issue: {e}")


# 4. main block

def main():
    # input from user
    summary = input("Enter the issue summary: ")
    description = input("Enter the issue description: ")    
    assignee = input("Enter the assignee (username): ")
    # call Create issue function
    create_issue(summary, description, assignee)

if __name__ == "__main__":
    main()