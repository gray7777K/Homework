grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
_students = list(students)
_students.sort()
print(_students)
average_grades = [round(sum(grade) / len(grade), 1) for grade in grades]
print(average_grades)
students_average = dict(zip(_students, average_grades))
print(students_average)