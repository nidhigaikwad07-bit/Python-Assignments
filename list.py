#Python program to perform operation on list

#Create and Access list elements
my_list = [10, 20, 30, 40, 50]
print("Initial List:", my_list)
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Add and Remove list elements
my_list.append(60)
print("\nAfter adding element:", my_list)

my_list.remove(30)
print("After removing element:", my_list)

# Sort list elements
my_list.sort()
print("\nSorted list:", my_list)

# Reverse list elements
my_list.reverse()
print("Reversed list:", my_list)