# Dictionary and Set

"""A dictionary in Python is a data structure 
    that stores information as key-value pairs. 
    The key describes or identifies the information,
    while the value is the actual information 
    associated with that key.
    """

# Dictionary 1: Student information
student = {
    "name": "Okechukwu",
    "age": 25,
    "course": "Python Programming",
    "city": "Bowie"
}

# Dictionary 2: Employee information
employee = {
    "name": "John",
    "position": "Software Engineer",
    "company": "Tech Solutions",
    "city": "Baltimore"
}

# Dictionary 3: Product information
product = {
    "name": "Laptop",
    "brand": "Lenovo",
    "price": 750,
    "category": "Electronics"
}

"""
    A set in Python is a collection of unique values. 
    This means that a set does not keep duplicate values. 
    For example, if I add Python multiple times to my skills set, 
    Python will only appear once.
"""
# Set 1: Programming skills
skills = {"Python", "Java", "Git", "Python", "SQL", "AI", "Java"}

# Set 2: Cities
cities = {"Bowie", "Baltimore", "Washington DC", "Annapolis"}

# Set 3: Technologies
technologies = {"Machine Learning", "AI", "Cloud Computing", "Data Science", "AI"}

# Display the dictionaries
print("Student Information:")
print(student)

print("\nEmployee Information:")
print(employee)

print("\nProduct Information:")
print(product)

# Display the sets
print("\nProgramming Skills:")
print(skills)

print("\nCities:")
print(cities)

print("\nTechnologies:")
print(technologies)