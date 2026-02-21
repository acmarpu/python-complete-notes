#------------------------------------------------------------------------------------------
 # un comment the code below and run it to see the output of the arithmetic operators
#-----------------------------------------------------------------------------------------

# Use the arithmetic operators to calculate the sum, average CPU load given cpu_loads = [ 40, 60, 80 ]

cpu_loads = [ 40, 60, 80 ]

print("CPU loads:", type(cpu_loads))

for load in cpu_loads:
    print("Individual CPU load:", load)
total_load = sum(cpu_loads)
average_load = total_load / len(cpu_loads)

# Sum of CPU loads: 180
print("\nSum of CPU loads:", total_load)

# Average CPU load: 60.0
print("Average CPU load:", average_load)


#------------------------------------------------------------------------------------------
# un comment the code below and run it to see the output of the comparison operators
#-----------------------------------------------------------------------------------------
# Use the comparison operators to check if disk usage is above 80%

# Input data : disk_usage = 85

disk_usage = 85

# Check if disk usage is above 80%
is_above_80 = disk_usage > 80

# Output: disk usage is above 80%: True
print("disk usage is above 80% :", is_above_80)


disk_usage = 75
is_above_80 = disk_usage > 80

# Output: disk usage is above 80%: False
print("disk usage is above 80% :", is_above_80)



#------------------------------------------------------------------------------------------
# un comment the code below and run it to see the output of the logical operators
#-----------------------------------------------------------------------------------------
# Use the logical operators (and, or, not) to check if (CPU > 70 amd Memory > 80)


# Input data : cpu_usage = 75, memory_usage = 85

cpu_usage = 75
memory_usage = 85

# Check if CPU > 70 and Memory > 80
cpu_condition01 = (cpu_usage > 70) and (memory_usage > 80)

# Output: System is compliant: True
print("\nCPU condition:", cpu_condition01)

cpu_usage = 60
memory_usage = 80

# Check if CPU > 70 and Memory > 80
cpu_condition02 = (cpu_usage > 70) and (memory_usage > 80)

# Output: System is compliant: False
print("\nCPU condition:", cpu_condition02)


# or operator
cpu_usage = 60
memory_usage = 85

# Check if CPU > 70 and Memory > 80
cpu_condition02 = (cpu_usage > 70) or (memory_usage > 80)

# Output: System is compliant: True
print("\nCPU condition:", cpu_condition02)



#------------------------------------------------------------------------------------------
# un comment the code below and run it to see the output of the identity operators
#-----------------------------------------------------------------------------------------

# Use the identity operator (is) to check if two services reference to the same object in memory

config = {"service": "web", "port": 80}
config2 = config
are_same_object = config is config2
# config and config2 reference the same object in memory: True
print("\nconfig and config2 reference the same object in memory:", are_same_object)


are_same_object = config is not config2
# config and config2 reference the same object in memory: False
print("\nconfig and config2 reference the same object in memory:", are_same_object)


#------------------------------------------------------------------------------------------
# un comment the code below and run it to see the output of the membership operators
#-----------------------------------------------------------------------------------------
# Use the membership operator (in) to check if a specific nginx is in running_services

running_services = ["nginx", "mysql", "redis"]
# Check if nginx is in running_services
is_nginx_running = "nginx" in running_services

# Output: nginx is running: True
print("nginx is running:", is_nginx_running)









