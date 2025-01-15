#  Write a Python program to iterate over a list using a for loop

list = [5, 10, 15, 20, 25]
print("Iterating over the list:")
for i in list:
    print(i)


# Write a Python program to sort a list using both sort() and sorted()

unsorted_list = [34, 12, 5, 78, 1]

unsorted_list.sort()
print("List after sort():", unsorted_list)

# ) Write a Python program to iterate through a list and print each element. 

elements = ["apple", "banana", "cherry"]

print("List elements:")
for item in elements:
    print(item)


# Write a Python program to insert elements into an empty list using a for loop and append().

empty_list = []

for i in range(1, 6):  
    empty_list.append(i)

print("List after appending elements:", empty_list)
