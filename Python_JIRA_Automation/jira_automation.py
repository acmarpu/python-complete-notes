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
def create_issue(summary, description):
    # create a new issue in JIRA (unassigned)
    issue_dict = {
        'project': {'key': PROJECT_KEY},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Task'},
    }
    try:
        new_issue = jira.create_issue(fields=issue_dict)
        print(f"Issue {new_issue.key} created successfully.")
        return new_issue.key
    except Exception as e:
        print(f"Error creating issue: {e}")
        return None

def assign_issue(issue_key, assignee_email):
    # Look up accountId for the given email
    try:
        users = jira.search_users(query=assignee_email)
        if not users:
            print(f"No JIRA user found for email: {assignee_email}")
            return
        account_id = users[0].accountId
        jira.assign_issue(issue_key, assignee=account_id)
        print(f"Issue {issue_key} assigned to {assignee_email}.")
    except Exception as e:
        print(f"Error assigning issue: {e}")


# 4. main block

def main():
    # input from user
    summary = input("Enter the issue summary: ")
    description = input("Enter the issue description: ")    
    assignee_email = input("Enter the assignee's email: ")
    # call Create issue function
    issue_key = create_issue(summary, description)
    if issue_key:
        assign_issue(issue_key, assignee_email)

if __name__ == "__main__":
    main()