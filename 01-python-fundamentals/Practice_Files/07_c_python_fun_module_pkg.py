# Write a function that takes a server's CPU & Memory usage and returns whether it's "Healthy" or "Critical" a server is concidered "critical" if either CPU usage is above 80% or memory usage is above 90%. Otherwise, it's "Healthy"

# input: cpu_usage = 85, memory_usage = 70
cpu_usage = 85
memory_usage = 70

# Driving factory

def check_server_health(cpu, memory):
    # condition to check if either CPU usage is above *80%  or Memory usage is above 90%
    if cpu > 86 or memory > 90:
        status = "Critical"
    else:
        status = "Healthy"
    
    return status

# Function Calling

server_status = check_server_health(cpu_usage, memory_usage)

#Output:
print(f"Server Status: {server_status}")