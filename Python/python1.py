MAB=7000
cibil_score=750
ACC_balance=10000
if MAB>5000 and cibil_score>700 and ACC_balance>5000:
    print("Eligible for loan")  
else:
    print("Not eligible for loan,Because either MAB is less than or equal to 5000, cibil_score is less than or equal to 700, or ACC_balance is less than or equal to 5000.")
# For loop to iterate through a range of numbers
for i in range(0, 10, 2):# Range function is used to generate a sequence of numbers. In this case, it generates numbers from 0 to 10 (exclusive) with a step of 2.
    print("The value of i is: ", i)
# while loop to iterate until a condition is met
i=0
while i<=10:
    print("The value of i is: ", i)
    i+=1    

#Array of numbers
numbers=[1,2,3,4,5,6,7,8,9,10]
# For loop to iterate through the array of numbers      
for num in numbers:
    print("The number is: ", num)   
#List of names- order is preserved in lists, indexes are used to access elements, and duplicates are allowed. Mutable,Hetrogeneous, dynamic in nature.  
names=["Alice","Bob","Charlie","David","Eve"]     
print("The 1st name is: ", names[0])  # Accessing the first name in the list using index 0
#slice to access a range of names in the list--> names[start_index:end_index:ste] where start_index is inclusive and end_index is exclusive
print("The names from index 1 to 3 are: ", names[1:])  # Accessing names from index 1 to the end of the list
print("The names from index 1 to 3 are: ", names[1:4])  # Accessing names from index 1 to 3 (4 is exclusive)
print("The names from index 0 to 2 are: ", names[:3])  # Accessing names from the start of the list to index 2 (3 is exclusive)
print("The names from index 2 to 4 are: ", names[2:5])  # Accessing names from index 2 to 4 (5 is exclusive)
#Adding a new name to the list using append() method
names.append("Frank")  # Adding a new name "Frank" to the end of the list
print("The updated list of names is: ", names)  # Printing the updated list of names
#Inserting a new name at a specific index using insert() method
names.insert(2, "Grace")  # Inserting a new name "Grace" at index 2 in the list
print("The updated list of names after insertion is: ", names)  # Printing the updated list of names after insertion
# For loop to iterate through the list of names
for name in names:
    print("The name is: ", name)
#Tuple of colors,order is preserved in tuples, indexes are used to access elements, and duplicates are allowed. Immutable,Hetrogeneous, dynamic in nature.
colors=("red","green","blue","yellow","orange")  
#Tuples are immutable, meaning that once they are created, their elements cannot be changed or modified. This makes tuples useful for storing data that should not be altered, such as coordinates or RGB values. Tuples can also be used as keys in dictionaries, whereas lists cannot. 
# Tuples are generally faster than lists for certain operations, such as iteration and membership testing, because they have a smaller memory footprint and are optimized for performance.
# Tuples can be used to return multiple values from a function, whereas lists can only return a single value. This makes tuples useful for functions that need to return multiple pieces of related data, such as a person's name and age.
# Slice to access a range of colors in the tuple--> colors[start_index:end_index:step] where start_index is inclusive and end_index is exclusive
print("The colors from index 1 to 3 are: ", colors[1:4])  # Accessing colors from index 1 to 3 (4 is exclusive)
print("The colors from index 0 to 2 are: ", colors[:3])  # Accessing colors from the start of the tuple to index 2 (3 is exclusive)
print("The colors from index 2 to the end are: ", colors[2:5])  # Accessing colors from index 2 to the end of the tuple
print("The colors from index 0 to the end are: ", colors[:])  # Accessing all colors in the tuple
print("The color at index 2 is: ", colors[2])  # Accessing the color at index 2 in the tuple
print("The color at index -1 is: ", colors[-1])  # Accessing the last color in the tuple using negative indexing
# For loop to iterate through the tuple of colors
for color in colors:
    print("The color is: ", color)
#Set of fruits
#sets are unordered collections of unique elements. They are mutable, meaning that you can add or remove elements from a set after it is created. Sets are useful for removing duplicates from a list or for performing mathematical operations such as union, intersection, and difference.
#sets are defined using curly braces {} or the set() constructor. Elements in a set can be of any immutable data type, such as numbers, strings, or tuples. However, sets cannot contain mutable elements such as lists or dictionaries.
#sets are unordered, meaning that the elements in a set do not have a specific order. This means that you cannot access elements in a set using an index, as you can with lists or tuples. Instead, you can iterate through the elements of a set using a for loop or convert the set to a list or tuple if you need to access elements by index.
#set does not allow duplicate elements. If you try to add a duplicate element to a set, it will be ignored. This makes sets useful for removing duplicates from a list or for checking if an element is already present in a collection.
fruits={"apple","banana","cherry","date","elderberry"}
#accessing elements in a set using a for loop
#Accessing elements in a set using a for loop is a common way to iterate through the elements of a set. Since sets are unordered collections, you cannot access elements by index. Instead, you can use a for loop to iterate through each element in the set and perform operations on them.
#To element is extracted from the set, it is removed from the set. This means that if you iterate through a set using a for loop and remove elements from the set during the iteration, you may encounter unexpected behavior. To avoid this, it is recommended to create a copy of the set before iterating through it if you need to modify the original set.
print("The set of fruits is: ", fruits)  # Printing the set of fruits
print("The length of the set of fruits is: ", len(fruits))  # Printing the length of the set of fruits
print("The type of the set of fruits is: ", type(fruits))  # Printing the type of the set of fruits
fruits.add("fig")  # Adding a new fruit "fig" to the set of fruits
print("The set of fruits after adding a fruit is: ", fruits)  # Printing the set of fruits after adding a fruit
fruits.remove("banana")  # Removing a fruit "banana" from the set of fruits     
print("The set of fruits after removing a fruit is: ", fruits)  # Printing the set of fruits after removing a fruit 
fruits.discard("grape")  # Discarding a fruit "grape" from the set of fruits (no error if not present)  
fruits.clear()  # Clearing all elements from the set of fruits
fruits={"apple","banana","cherry","date","elderberry"}  # Re-initializing the set of fruits 
fruits.pop()  # Removing and returning an arbitrary element from the set of fruits
print("The set of fruits after popping an element is: ", fruits)  # Printing the set of fruits after popping an element
# For loop to iterate through the set of fruits
for fruit in fruits:
    print("The fruit is: ", fruit)
#Dictionary of countries and their capitals 
#Dictionaries are unordered collections of key-value pairs. They are mutable, meaning that you can add, remove, or modify elements in a dictionary after it is created. Dictionaries are useful for storing and retrieving data based on a unique key, such as a name or ID number.
#Dictionaries are defined using curly braces {} or the dict() constructor. Each key-value pair
# in a dictionary is separated by a colon (:), and each pair is separated by a comma. Keys in a dictionary must be unique and immutable, such as strings, numbers, or tuples. Values in a dictionary can be of any data type, including other dictionaries.
#Dictionaries are unordered, meaning that the elements in a dictionary do not have a specific order. This means that you cannot access elements in a dictionary using an index, as you can with lists or tuples. Instead, you can access values in a dictionary using their corresponding keys.
countries={"USA":"Washington D.C.","India":"New Delhi","UK":"London","France":"Paris","Germany":"Berlin"}
#Adding a new country and its capital to the dictionary using the key-value pair
countries["Japan"]="Tokyo"  # Adding a new country "Japan" with its capital "Tokyo" to the dictionary
print("The updated dictionary of countries and their capitals is: ", countries)  # Printing the
# updated dictionary of countries and their capitals
# Removing a country and its capital from the dictionary using the key
#Setting a" default value for a key that may not exist in the dictionary using the get() method
capital_of_italy=countries.get("Italy","Capital not found")  # Getting the capital of Italy from the dictionary, with a default value if the key does not exist
print("The capital of Italy is: ", capital_of_italy)  # Printing the capital of Italy
countries.pop("Germany")  # Removing the country "Germany" and its capital from the dictionary
print("The updated dictionary of countries and their capitals after removing Germany is: ", countries)
# For loop to iterate through the dictionary of countries and their capitals
for country, capital in countries.items():
    print("The capital of {} is {}".format(country, capital))

list1=["A","B","C","D","E"]
for i in range(len(list1)):
    print("The element at index {} is {}".format(i, list1[i]))  


x=true  # Assigning a boolean value True to the variable x
print("The value of x is: ", x)  # Printing the value of x
