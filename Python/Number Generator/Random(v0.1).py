import random as rn

print('       |РАНДОМАЙЗЕР ЧИСЕЛ|\n    |Введите диапазон от и до|')
ot=int(input('>>'))
do=int(input('>>'))
try:
   print(f'|Ваше случайное число:{rn.randrange(ot, do)}|')
except ValueError:
    print('   |Значение "от" не может быть больше значения "до". Перезапустите программу|')




