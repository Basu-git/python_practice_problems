#8. Create a nested dictionary of students (id: {name, age, marks}). Print only names of students.
students = {
    101: {"name": "Alice", "age": 20, "marks": 85},
    102: {"name": "Bob", "age": 21, "marks": 78},
    103: {"name": "Charlie", "age": 19, "marks": 92},
    104: {"name": "David", "age": 22, "marks": 74},
    105: {"name": "Eva", "age": 20, "marks": 88}
}
for student in students.values():
    print(student["name"])