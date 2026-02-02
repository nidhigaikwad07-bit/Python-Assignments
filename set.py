# Python program to perform operation on Set
# Create and access set elements
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print("Set 1:", set1)
print("Set 2:", set2)

# Union of the elements
union_set = set1.union(set2)
print("\nUnion:", union_set)

# Intersection of the elements
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference of the elements
difference_set = set1.difference(set2)
print("Difference (Set1 - Set2):", difference_set)