try:
    with open("sample-1.txt", "r") as file:
        for line in file:
            print(line, end="")
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
