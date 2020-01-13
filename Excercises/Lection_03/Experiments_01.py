from datetime import datetime


# ----------------------
# Function to print date and time;
def print_time(initials):
    def wrapper(a, b, c):
        print('Please tell me your initials')
        initials(a, b, c)
        print(datetime.now())
    return wrapper


# ---------------------
# Make functions for initials
def get_initial(name):
    initial = name[0:1].upper()
    return initial


# ---------------------
# Ask question;
first_name = input('Enter your First name: ')
first_name_initials = get_initial(first_name)

middle_name = input('Enter your Middle name: ')
middle_name_initials = get_initial(middle_name)

last_name = input('Enter your Last name: ')
last_name_initials = get_initial(last_name)


@print_time
def initials(a, b, c):
    print(a + b + c)


initials(first_name_initials, middle_name_initials, last_name_initials)
