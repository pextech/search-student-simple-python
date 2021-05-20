import re

def password_validate():
    count_trial = 3
    while True and count_trial > 0:
        password = input("Enter a password: ")
        special_char_check = re.compile('[@_#$%^&*()<>?/|}{~:]')

        if len(password) < 8:
            count_trial -= 1
            print("Make sure your password is at lest 8 letters ({0} trials left!!)".format(count_trial))

        elif special_char_check.search(password) == None:
            count_trial -= 1
            print("Password should atleast contain a special character in it ({0} trials left!!)".format(count_trial))

        elif re.search('[a-z]', password) is None:
            count_trial -= 1
            print("Make sure your password has a lower letter in it ({0} trials left!!)".format(count_trial))

        elif not any(character.isupper() for character in password):
            count_trial -= 1
            print("Make sure your password has a capital letter in it ({0} trials left!!)".format(count_trial))

        elif re.search('[0-9]', password) is None:
            count_trial -= 1
            print("Make sure your password has a number in it ({0} trials left!!)".format(count_trial))

        else:
            return password
