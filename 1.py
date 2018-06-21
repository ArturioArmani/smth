small = int(input("Количество бутилок меньше 1 л: "))
big = int(input("Количество бутилок больше равно 1 л: "))
money = small * 0.10 + big * 0.25
print('общая стоимость:',money,'$')

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Бойко Артур'
printTimeStamp(name)
