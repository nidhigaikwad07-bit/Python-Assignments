# Python program to perform operation on Tuple

# Create and access tuple
my_tuple = (10, 20, 30, 40)
print("Initial Tuple:", my_tuple)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Nested Tuple
nested_tuple = (1, 2, (3, 4), 5)
print("\nNested Tuple:", nested_tuple)

# Repetition of tuple
repeated_tuple = my_tuple * 2
print("\nRepeated Tuple:", repeated_tuple)

# Concatenation of tuples
tuple2 = (50, 60)
concatenated_tuple = my_tuple + tuple2
print("\nConcatenated Tuple:", concatenated_tuple)