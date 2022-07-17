""" Task 5.3
File `data/students.csv` stores information about students in [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
This file contains the student’s names, age and average mark.
1) Implement a function which receives file path and returns names of top performer students
```python
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))
['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']

2) Implement a function which receives the file path with students info and writes CSV student information to the new file in descending order of age.
Result:

student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
"""


def get_top_performers(file_path, number_of_top_students=5):
    students = get_students_from_file(file_path)
    students.sort(key=lambda student: student[2], reverse=True)
    students = students[:number_of_top_students]
    return [student[0] for student in students]


def write_students_sorted_by_age(source_file_path, target_file_path):
    students = get_students_from_file(source_file_path)
    students.sort(key=lambda student: student[1], reverse=True)
    students = [(student[0], str(student[1]), str(student[2])) for student in students]
    content = [",".join(student) for student in students]
    content.insert(0, "student name,age,average mark")
    content = "\n".join(content)
    file = open(target_file_path, "w")
    file.write(content)


def get_students_from_file(file_path):
    file = open(file_path)
    content = file.read()
    if not content:
        return

    students_data = content.split("\n")
    students_data = students_data[1:]
    students = [student.split(",") for student in students_data]
    return [(student[0], int(student[1]), float(student[2])) for student in students if len(student) == 3]


print(get_top_performers("data/students.csv"))

write_students_sorted_by_age("data/students.csv", "data/sorted_students.csv")
