#Lab:
# Write a Python program to update a value in a dictionary.


my_dict = {"name": "Khush", "age": 20, "course": "IT"}


my_dict["age"] = 25 
print("Updated Dictionary:", my_dict)

# Write a Python program to merge two lists into one dictionary using a loop.


keys = ["name", "age", "course"]
values = ["Khush", 20, "IT"]

merged_dict = {}
for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

print("Merged Dictionary:", merged_dict)

# 15) Write a Python program to update a value at a particular key in a

my_dict = {"name": "Khush", "age": 20, "course": "IT"}
my_dict["course"] = "Data Science"  
print("Updated Dictionary:", my_dict)

# 16) Write a Python program to separate keys and values from a dictionary using keys() and values() methods. 


my_dict = {"name": "Khush", "age": 20, "course": "IT"}

keys = my_dict.keys()
values = my_dict.values()

print("Keys:", list(keys))
print("Values:", list(values))

#17) Write a Python program to convert two lists into one dictionary using a for loop. 

keys = ["name", "age", "course"]
values = ["Khush", 20, "IT"]

merged_dict = {}
for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

print("Dictionary:", merged_dict)

#18) Write a Python program to count how many times each character appears in a string.

# Input string
input_string = "hello world"

char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character Count:", char_count)

