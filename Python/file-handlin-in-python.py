#File handling in python
##Opening a file,creating a file,reading a file,writing a file,closing a file
#In Python, file has 4 modes:create(x), read(r), write(w), append(a), read and write(r+) and each mode has its own purpose.
#Example of opening a file
#file = open("sample-1.txt", "x")  # Creates a new file named "example.txt" in write mode
#file.close()  # Close the file
# newline \n, space \s, tab \t, carriage return \r, backspace \b, form feed \f, vertical tab \v
file = open("sample-1.txt", "w")  # Opens the file in write mode
file.write("Hello, this is a sample file.\n")  # Write some content to the file
file.write("This file is created for demonstration purposes.\n")
file.close()  # Close the file

##Appending to a file
file = open("sample-1.txt", "a")  # Opens the file in append mode
file.write("This line is appended to the file.\n")  # Append a new line 
file.close()  # Close the file

#Reading a file
file = open("sample-1.txt", "r")  # Opens the file in read mode
content = file.read()  # Read the content of the file
print(content)  # Print the content
file.close()  # Close the file  

server ={
    "Jenkins": "running",
    "Docker": "running",
    "Kubernetes": "stopped",
    "Nginx": "stopped",
}

def check_server_status(server): 
    final_status = {}   
    for i in server.keys():
        if server[i] != "running":
            final_status[i] = server[i]
    return final_status

result = check_server_status(server)
for server_name, status in result.items():
    print(f"{server_name} is {status}. Please check the server.")

def check_disk_health(disk_health):
    final_status = {}
    for i in disk_health.keys():
        if disk_health[i] >80:
            final_status[i] =str(disk_health[i]) + " Warning: Disk health is above 80%. Please check the disk."
        else:
            final_status[i] = str(disk_health[i]) + " Disk health is normal."
    return final_status

disk_health = {
    "Disk1": 56, 
    "Disk2": 89,
    "Disk3": 98
}

result = check_disk_health(disk_health)
for disk_name, status in result.items():
    print(f"{disk_name} is {status}")