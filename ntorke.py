from csv import reader

with open('rezultati.csv', 'r', encoding="utf8") as read_obj:
    csv_reader = reader(read_obj)
    students = list(map(tuple, csv_reader))

students.sort(key=lambda el: el[1])

grades_dict = {}

def calculate_grade(score):
    if score >= 90:
        return 'Izvrstan'
    elif score >= 80:
        return 'Vrlo dobar'
    elif score >= 65:
        return 'Dobar'
    elif score >= 50:
        return 'Dovoljan'
    else:
        return 'Nedovoljan'

for student in students:
    last_name = student[1]
    score = int(student[2])
    grade = calculate_grade(score)
    
    if grade in grades_dict:
        grades_dict[grade] += 1
    else:
        grades_dict[grade] = 1

print(students)
print(grades_dict)
