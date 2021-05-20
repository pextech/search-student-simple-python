import validate_password
import submit_password


def line_handler(count_lines, file, id_term):
    for line in file:
        count_lines += 1
        if id_term not in line and count_lines > 2:
            print('wrong id')

        elif id_term in line:
            print("logged in user: ", line)

            # validating password
            user_password = validate_password.password_validate()

            # submit handler
            submit_password.submit_handler(user_password, line)
