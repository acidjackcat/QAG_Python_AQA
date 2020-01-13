"""Задача 1: У магазин завезли 8 ящиків огірків по 12кг у кожному. За день
продали 57 кг. Скільки кг огірків залишилось?"""

cucumber_box_weight = 12
daily_sale = 57
cucumber_leftovers = (cucumber_box_weight * 8) - daily_sale
print(cucumber_leftovers)

"""Lets solve this task as function"""
"""Function for solving task:"""


def cucumber_leftovers(cucumber_box_weight, daily_sale, cucumber_boxes_total):
    return (cucumber_box_weight * cucumber_boxes_total) - daily_sale


"""Request for input new values for out task:"""

cucumber_box_weight = int(input('Enter weight of one box with cucumbers: '))
cucumber_boxes_total = int(input('Enter total number of boxes: '))
daily_sale = int(input('Enter quantity of sold cucumbers in kg: '))

print(f'Your leftovers in kg for today is: '
      f'{cucumber_leftovers(cucumber_box_weight, daily_sale, cucumber_boxes_total)}')
