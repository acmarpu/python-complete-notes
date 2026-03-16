'''
#  ------------------------------------------------------------
   # while loop example : multiplication table
#  -------------------------------------------------------------
# input from user
num = int(input("enter a number to print its multiplication table: "))

# initialize counter

i = 1
print(f"Multiplication Table of {num}:")

# while loop from 1 to 10
while i <= 10:
    product = num * i
    print(f"{num} X {i} = {product}")
    i += 1  # increment counter



# DevOps Use Case: Monitoring Service with basic loop

import random
import time

services = ['web_server', 'database', 'cache', 'message_queue']
# Service_index = 0           1           2          3

Service_index = 0 

while Service_index < len(services):
    service = services[Service_index]
    # SImulate checking service status
    status = random.choice(['running', 'stopped', 'degraded'])
    print(f"Service: {service}, status {status}")
    Service_index += 1
    time.sleep(1) # wait for 1 second before checking next service 



# ------------------------------------------------------------
  # For Loop example :
# ------------------------------------------------------------

import time
# for loop example :
# loops help automate tasks across multiple servers

servers = ["server1", 'server2', 'server3']
for server in servers:
    # simulate deploying an update
    print(f"Deployong update to {server}....")
    time.sleep(1) # simulate time taken to deploy
    print(f"Update deployed to {server}.")


# ------------------------------------------------------------
  # Break and Continue in loop
# ------------------------------------------------------------

# Example: Monitoring CPU usage and alerting if it exceeds threshold
cpu_usages = [45, 55, 65, 75, 85, 95, 100]
threshold = 90

for usage in cpu_usages:
    if usage > 75:
        print(f"error: invalid CPU usage reaing: {usage}%. skip this")
        continue # Skip invalid readigs 
    
    if usage > threshold:
        print(f"Alert! High CPU usage detected: {usage}%")
        break # exit loop on critical alert 
    
    print(f"CPU usage is normal: {usage}%")




# ------------------------------------------------------------
  # for loop
# ------------------------------------------------------------
import os

servers = ['srv1', 'srv2', 'srv3']

for server in servers:
    response = os.system('echo ' + server)  # ping each server once
    if response == 0:
        print(f'{server} is up')
    else:
        print(f'{server} is dowm')

'''
# ------------------------------------------------------------
  # for loop break and continue 
# ------------------------------------------------------------
import os

servers = ['srv1', 'srv2', 'srv3']

for server in servers:
    if server == 'srv2':
        print('Skipping server srv2')
        continue # skip the rest of the loop for this iteration
    response = os.system('echo ' + server)  # ping each server once
    if response == 0:
        print(f'{server} is up')
        break  # exit the loop if a server is up
    else:
        print(f'{server} is dowm')

# ------------------------------------------------------------
  # range
# ------------------------------------------------------------

for i in range(1, 11):  # loop from 1 to 10
    print(f"5 X {i} = {5 * i}")