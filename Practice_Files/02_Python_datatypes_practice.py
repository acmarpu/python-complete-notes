#------------------------------------------------------------
# Practic Question 1
#------------------------------------------------------------

# convert a list of servers IPs into a tuple amd explain why immutability is preferable

# input: list of servers IPs
servers_list = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4"]

# convert list to tuple
servers_tuple = tuple(servers_list)

# Expected output: Tuple of servers IPs: Tuple of servers IPs: ('192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4')
print("Tuple of servers IPs:", servers_tuple)

# explain why immutability is preferable
print("\nWhy immutability is preferable:")
print("- Tuples are immutable, so they cannot be changed after creation.")
print("- This prevents accidental modification of data.")
print("- Tuples are faster than lists for accessing elements.")
print("- They are useful for representing fixed collections of data like IP addresses.")

#------------------------------------------------------------
# Practic Question 2
#------------------------------------------------------------

# Convert CPU usage from string  "78.5" to float and compare with a threshold (e.g 80.0)

cpu_usage_str = "78.5"

# Expected Output: CPU usage as string: 78.5 <class 'str'>
print("\nCPU usage as string:", cpu_usage_str, type(cpu_usage_str))

# Convert string to float
cpu_usage_float = float(cpu_usage_str)
# Expected Output: CPU usage as float: 78.5 <class 'float'>
print("\nCPU usage as float:", cpu_usage_float, type(cpu_usage_float))


threshold = 80.0
# Compare CPU usage with threshold
is_above_threshold = cpu_usage_float > threshold

# Expected Output: Is CPU usage above threshold? False
print("\nIs CPU usage above threshold?", is_above_threshold)


#------------------------------------------------------------
# Practic Question 3
#------------------------------------------------------------

# Access the first 3 servers IPs from a lsit using slicing 

server_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5"]

# Access the first 3 servers IPs using slicing
first_three_ips = server_ips[:3]

# Expected Output: First 3 servers IPs: ['192.168.1.1', '192.168.1.2', '192.168.1.3']
print("\nFirst 3 servers IPs:", first_three_ips)
print("First 3 servers IPs:", type(first_three_ips))


#------------------------------------------------------------
# Practic Question 3
#------------------------------------------------------------

# From a log message string "ERROR: Pod crashed at 10:00, slice to get only "ERROR"

log_message = "2025-06-01 10:00:00 ERROR: Pod crashed"
# Slice the log message to get only "ERROR"
error_message = log_message[20:25]  # Extract substring from index 20 to 25 (inclusive)
print("\n sliced error message:", error_message)



#------------------------------------------------------------
# Practic Question 4
#------------------------------------------------------------
"""
Extract every alterante and reverse service name from a list of services.

    services = ["nginx", "redis", "mysql", "postgres", "mongodb", "kafka", "elasticsearch"]
"""

services = ["nginx", "redis", "mysql", "postgres", "mongodb", "kafka", "elasticsearch"]

alternate_reverse_services = services[::-2]

# Alternate and reverse service names: ['elasticsearch', 'mongodb', 'mysql', 'nginx']
print("\nAlternate and reverse service names:", alternate_reverse_services)

