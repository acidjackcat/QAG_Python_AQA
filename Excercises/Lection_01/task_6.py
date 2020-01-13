"""Задача 6 - написана у вигляді функції:"""

def task_6(chair_cover, chairs_in_fabric_piece, chairs_in_sofa_fabric):

    return (chair_cover * chairs_in_fabric_piece) // (chair_cover *
                                                      chairs_in_sofa_fabric)

chair_cover = int(input(f'Enter size of chair cover: '))
chairs_in_fabric_piece = int(input(f'Enter quantity of chair covers in '
                                       f'one piece of fabric: '))
chairs_in_sofa_fabric = int(input(f'Enter in how times the sofa fabric '
                                      f'should be bigger than sofa: '))
print(f'You can make this number of sofa  '
      f'{task_6(chair_cover, chairs_in_fabric_piece, chairs_in_sofa_fabric)}')
