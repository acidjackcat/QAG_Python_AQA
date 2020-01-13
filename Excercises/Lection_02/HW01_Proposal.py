from datetime import datetime
name = 0


def proposal_decorator(func):
    def wrapper():
        print(f"\n\nДиректору ТзОВ “Роги і Копита \nСкоробагатьку П. С. "
              f"\n\n\tЗаява")
        func()
    return wrapper


@proposal_decorator
def vacation():
    """Vacation request:"""
    print(f"\n\nЯ, {name}, прошу надати мені відпустку терміном на 14 днів. "
          f"\n {datetime.now()}")


@proposal_decorator
def sick_leave():
    """Sick Leave request:"""
    print(f"\n\nЯ, {name}, прошу надати мені лікарняний на термін вказаний у "
          f"додатку від лікаря. "
          f"\n {datetime.now()}")


@proposal_decorator
def dismissal():
    """Dismissal request:"""
    print(f"\n\nЯ, {name}, прошу звільнити мене за власним бажанням."
          f"\n {datetime.now()}")


def printer():
    print("Hallo, i'm DocuHelper, your document assistant! What is your name?")
    name = input("My name is: ")
    print(f"Nice to meet you {name}! \nIf you would like to take Vacation: "
          f"enter number 1. \nIf you would like to take Sick Leave: enter number "
          f"2. \nIf you would like to Left your Job: enter number 3")
    choice = input("Please, enter desired number here: ")
    if choice == "1":
        vacation()
    elif choice == "2":
        sick_leave()
    elif choice == "3":
        dismissal()
    else:
        print('Please enter correct number')


printer()