import check_updated

def updated_students(student):
    new_students = []
    new_students.append(student)
    new_file = open("final_students.txt", "a")

    for student in new_students:
        new_file.write(student + '\n')
