# Python program to perform operation on Dictionary

# Create and access dictionary elements
student = {
    "roll_no": 101,
    "name": "Amit",
    "marks": 85
}

print("Initial Dictionary:", student)
print("Name:", student["name"])
print("Marks:", student["marks"])

# Update Dictionary
student["marks"] = 90
student["grade"] = "A"
print("\nAfter Updating Dictionary:", student)

# Removing Elements
removed_item = student.pop("roll_no")
print("\nRemoved roll_no:", removed_item)
print("Dictionary after removal:", student)

# Merging Dictionaries
extra_info = {
    "age": 20,
    "city": "Mumbai"
}

student.update(extra_info)
print("\nAfter Merging Dictionaries:", student)