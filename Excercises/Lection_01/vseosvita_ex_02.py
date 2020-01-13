"""Умова задачі 02: На пошив фартука бабуся відрізала з мотка 5 шматочків
стрічки по 9 дм у кожному. У мотку залишилось 20 дм стрічки. Скільки дм 
стрічки було у мотку із початку?"""

# 1) порахуємо скільки загалом було використано стрічки на пошив фартуха
"""length_of_strings = 9
pieces_of_string = 5
leftovers_of_string = 20
strings_for_apron = length_of_string * pieces_of_string"""
# 2) порахуємо загальну довжину мотка
"""total_length_strings = strings_for_apron + leftovers_of_string
print(total_length_strings)"""


"""Вирішимо задачу за допомогою функції:"""


def total_length_strings(length_of_strings, pieces_of_string,
                         leftovers_of_string):
    strings_for_apron = length_of_strings * pieces_of_string
    return strings_for_apron + leftovers_of_string


length_of_strings = int(input(f'Enter length of one string: '))
pieces_of_string = int(input(f'Enter number of string for one apron: '))
leftovers_of_string = int(input(f'Enter number of leftovers: '))

print(f'Total length of all strings is {total_length_strings(length_of_strings, pieces_of_string, leftovers_of_string)}')