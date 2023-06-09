# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

from random import randint
bush = list(randint(1, 20)
            for i in range(int(input('Введите кол-во кустов: '))))
print(f'Количество ягод на каждом кусте', bush)
a = int(input('Введите № куста: '))
res = 0
if a == 1:
    res = bush[0] + bush[1] + bush[-1]
elif a == len(bush):
    res = bush[-2] + bush[-1] + bush[0]
else:
    res = bush[a-1] + bush[a-2] + bush[a]
print(f"Максимальное число ягод за однин заход равно:  {res}")
