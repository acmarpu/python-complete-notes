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

# Read issue function
def is_valid_issue_key(issue_key):
    return bool(re.match(r"^[A-Z][A-Z0-9]+-\d+$", issue_key.strip()))


def read_issue(issue_key):
    issue_key = issue_key.strip()
    if not issue_key:
        print("Issue key is required.")
        return
    if not is_valid_issue_key(issue_key):
        print("Invalid issue key format. Enter a JIRA issue key like PROJECT-123.")
        return

    try:
        issue = jira.issue(issue_key)
        print(f"Issue Key: {issue.key}")
        print(f"Summary: {issue.fields.summary}")
        print(f"Description: {issue.fields.description}")
        print(f"Status: {issue.fields.status.name}")
    except Exception as e:
        print(f"Error reading issue: {e}")


def get_issue_status(issue_key):
    issue_key = issue_key.strip()
    if not issue_key:
        print("Issue key is required.")
        return
    if not is_valid_issue_key(issue_key):
        print("Invalid issue key format. Enter a JIRA issue key like PROJECT-123.")
        return

    try:
        issue = jira.issue(issue_key)
        print(f"Issue {issue.key} status: {issue.fields.status.name}")
    except Exception as e:
        print(f"Error reading issue status: {e}")


def list_todo_inprogress_issues():
    statuses = ["To Do", "In Progress"]
    jql_status = ",".join(f'"{status}"' for status in statuses)
    jql = f'project = {PROJECT_KEY} AND status in ({jql_status}) ORDER BY status, key'

    try:
        issues = jira.search_issues(jql, maxResults=100)
        if not issues:
            print("No issues found in To Do or In Progress.")
            return

        print(f"Issues in To Do / In Progress for project {PROJECT_KEY}:")
        for issue in issues:
            print(f"- {issue.key}: {issue.fields.status.name} - {issue.fields.summary}")
    except Exception as e:
        print(f"Error listing issues by status: {e}")


def change_issue_status(issue_key, new_status):
    issue_key = issue_key.strip()
    new_status = new_status.strip()

    if not issue_key:
        print("Issue key is required.")
        return
    if not new_status:
        print("New status is required.")
        return
    if not is_valid_issue_key(issue_key):
        print("Invalid issue key format. Enter a JIRA issue key like PROJECT-123.")
        return

    try:
        issue = jira.issue(issue_key)
        if issue.fields.status.name.lower() == new_status.lower():
            print(f"Issue {issue_key} is already in status '{issue.fields.status.name}'.")
            return

        available_transitions = jira.transitions(issue)
        target_transition = next((t for t in available_transitions if t["name"].lower() == new_status.lower()), None)

        if not target_transition:
            print(f"Status '{new_status}' is not a valid transition for issue {issue_key}.")
            print("Available statuses:")
            for transition in available_transitions:
                print(f"- {transition['name']}")
            return

        jira.transition_issue(issue, target_transition["id"])
        print(f"Issue {issue_key} transitioned to '{new_status}' successfully.")
    except Exception as e:
        print(f"Error changing issue status: {e}")


def change_issue_status_from_todo(issue_key):
    issue_key = issue_key.strip()

    if not issue_key:
        print("Issue key is required.")
        return
    if not is_valid_issue_key(issue_key):
        print("Invalid issue key format. Enter a JIRA issue key like PROJECT-123.")
        return

    try:
        issue = jira.issue(issue_key)
        current_status = issue.fields.status.name
        status_lower = current_status.lower()

        if status_lower in ["to do", "todo"]:
            print("Current status is To Do. Select the next status:")
            print("1 - In Progress")
            print("2 - Done")
            choice = input("Enter choice (1-2): ").strip()
            if choice == "1":
                new_status = "In Progress"
            elif choice == "2":
                new_status = "Done"
            else:
                print("Invalid choice. Please enter 1 or 2.")
                return
        elif status_lower == "in progress":
            print("Current status is In Progress. Select the next status:")
            print("1 - Done")
            choice = input("Enter choice (1): ").strip()
            if choice == "1":
                new_status = "Done"
            else:
                print("Invalid choice. Please enter 1.")
                return
        else:
            print(f"Issue {issue_key} is in '{current_status}' and cannot be advanced using this option.")
            return

        print(f"Changing issue {issue_key} from '{current_status}' to '{new_status}'.")
        change_issue_status(issue_key, new_status)
    except Exception as e:
        print(f"Error changing issue status from To Do: {e}")


# 4. main block

def main():
    print("JIRA Automation")
    print("1 - Create issue")
    print("2 - List all To Do and In Progress issues")
    print("3 - Read issue details")
    print("4 - Get issue status")
    print("5 - Update issue")
    print("6 - Advance issue status")

    choice = input("Enter choice (1-6): ").strip()

    if choice == "1":
        summary = input("Enter the issue summary: ").strip()
        description = input("Enter the issue description: ").strip()
        create_issue(summary, description)

    elif choice == "2":
        list_todo_inprogress_issues()

    elif choice == "3":
        read_issue_key = input("Enter the JIRA issue key to read (e.g. PROJECT-123): ")
        read_issue(read_issue_key)

    elif choice == "4":
        issue_key = input("Enter the JIRA issue key to get status (e.g. PROJECT-123): ")
        get_issue_status(issue_key)

    elif choice == "5":
        issue_key = input("Enter the JIRA issue key to update (e.g. PROJECT-123): ")
        assignee_email = input("Enter the email of the user to assign the issue to: ")
        assign_issue(issue_key, assignee_email)

    elif choice == "6":
        issue_key = input("Enter the JIRA issue key to advance (To Do -> In Progress, In Progress -> Done) (e.g. PROJECT-123): ")
        change_issue_status_from_todo(issue_key)

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
   



if __name__ == "__main__":
    main()
  