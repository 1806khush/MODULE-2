#  Write a Python program to add elements to a list using insert() and append().

# Adding elements 
my_list = [1, 2, 3]

my_list.append(4)
print("List after append:", my_list)
my_list.insert(1, 10)
print("List after insert:", my_list)



#  Write a Python program to remove elements from a list using pop() and remove().

my_list = [1, 10, 2, 3, 4]

my_list.remove(10)
print("List after remove:", my_list)

removed = my_list.pop(2)  
print("List after pop:", my_list)
print("Popped element:", removed)



# 3) Write a Python program to update a list using insert() and append().

update_list = ["a", "b", "c"]

update_list.append("d")

update_list.insert(2, "x")  

print("Updated list:", update_list)


# 4) Write a Python program to remove elements from a list using pop() and remove().

remove_list = [5, 10, 15, 20, 25]

remove_list.remove(15)

removed_value = remove_list.pop(3) 

print("List after removals:", remove_list)
print("Removed value with pop:", removed_value)

