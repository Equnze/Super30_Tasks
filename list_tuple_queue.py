# List, Tuple, and Queue

"""A list is a collection of multiple items stored
in one variable. Lists use square brackets []. And is mutable.
"""


programming_skills = ["Python", "Git", "SQL","AI", "Machine Learning"]


students = ["John", "Mary", "David", "Sarah"]


python_topics = ["Variables", "Strings", "Lists", "Dictionaries"]

"""A tuple is a collection of multiple items stored
in one variable. Tuples use parentheses (). And it is immutable.
"""


training_location = ("Bowie", "Maryland", "USA")


course_info = ("Python Programming", "Beginner", "8 Weeks")


instructor_info = ("Okechukwu", "Python Instructor", "Maryland")

"""A queue represents items waiting to be processed.
Queues use lists and follow the First-In-First-Out (FIFO) principle.
"""

student_queue = ["John", "Mary", "David"]


grading_queue = ["Assignment 1", "Assignment 2", "Assignment 3"]


class_queue = ["Python Basics", "Data Structures", "Functions"]

print("LIST EXAMPLES")
print(programming_skills)
print(students)
print(python_topics)

print("\nTUPLE EXAMPLES")
print(training_location)
print(course_info)
print(instructor_info)

print("\nQUEUE EXAMPLES")
print(student_queue)
print(grading_queue)
print(class_queue)

"""In summary, lists are useful for collections of information that may change,
tuples are useful for collections that should remain fixed,
and queues are useful when information or tasks need to be
processed in First In, First Out order."""