import updated


def submit_handler(user_password, line):
    if user_password != None:

        user_password = user_password.replace('+', '')
        user_password = user_password.replace('!', '')
        user_password = user_password.replace('=', '')


        password_term = ",password:" + user_password

        for each_character in password_term:
            line = line.rstrip() + each_character
        print("updated user: " + line)
        updated.updated_students(line)

    else:
        print("Invalid password")
