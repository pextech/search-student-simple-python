import check_line

user_id = input("Please Enter your Id: ")
id_term = "id:" + user_id
count_lines = 0

if user_id != '' and len(user_id) > 2:
    try:
        file = open("students.txt", "r")

        # check each line
        check_line.line_handler(count_lines, file, id_term)

        # close the file
        file.close()

    except FileNotFoundError as file_not_found:
        print("The file doesn't exist")

else:
    print("Getta outta here")
