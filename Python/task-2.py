# 1. Take user input and write it to output.txt
user_data = input("Enter data to write: ")
with open("output.txt", "w") as file:
    file.write(user_data + "\n")

# 2. Append additional data to the same file
additional_data = "This is appended data."
with open("output.txt", "a") as file:
    file.write(additional_data + "\n")

# 3. Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read(), end="")
