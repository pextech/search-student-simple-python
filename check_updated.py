def check_updated_students(line_to_check):
    file = open("final_students.txt", "r")

    for lines in file:
        if line_to_check not in lines:
            return True

        elif line_to_check in lines:
            return False

