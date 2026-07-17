

#  Read/write files
with open("sample.txt","w") as file:
    file.write("Hello, World!")
 

# Append to files
with open("sample.txt","a") as file:
    file.write("\nThis is an additional line.")


#  Read files
with open("sample.txt","r") as file:
    content = file.read()
    print(content)


#  Use config files
# Types of config files: use .env files 
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
print(f"API Key: {api_key}")


git_token = os.getenv("GITHUB_TOKEN")
print(f"GitHub Token: {git_token}")


# Using configparser ini files
import configparser
config = configparser.ConfigParser()
config.read("config.ini")

env= 'dev'
print("Section:', config.sections())")
print("database User:", config[env + '_db_config']['DB_USER'])
print("database Password:", config[env + '_db_config']['DB_PASSWORD'])
print("database Host:", config[env + '_db_config']['DB_HOST'])
print("database Port:", config[env + '_db_config']['DB_PORT'])


# Use YAML FIles

import yaml
with open("./Practice_Files/config.yaml", "r") as file:
    config = yaml.safe_load(file)

print("YAML Config:")
print(config)   
print("Database User from YAML file:", config['dev_db_config']['DB_USER'])
print("Database Password from YAML file:", config['dev_db_config']['DB_PASSWORD'])
print("Database Host from YAML file:", config['dev_db_config']['DB_HOST'])
print("Database Port from YAML file:", config['dev_db_config']['DB_PORT'])


# Use JSON FIles
import json
with open("./Practice_Files/config.json", "r") as file:
    config = json.load(file)

print("JSON Config:")
print(config)
print("Database User from JSON file:", config['dev_db_config']['username'])
print("Database Password from JSON file:", config['dev_db_config']['password'])
print("Database Host from JSON file:", config['dev_db_config']['host'])
print("Database Port from JSON file:", config['dev_db_config']['port'])

