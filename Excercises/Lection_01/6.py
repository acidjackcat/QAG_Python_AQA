print('Скільки метрів містить кусок тканини для твого крісла:')
chair_cover = int(input())
fabric_piece = chair_cover * 12
print(f'Розмір шматка тканини: {fabric_piece}')
sofa_cover = chair_cover * 2

print(f'Кількість чохлів для дивану із шматка тканини є:'
    f' {fabric_piece // sofa_cover}')