import math
food = int(input('Вартість їжі:'))
chay = food/100 * 14
podatok = food/100 * 18
a = chay
b = podatok
print ('Чайові:',a,'$','Податок:',b,'$')
summa = (food + a + b)
print ('Загальна сума оплати:',summa,'$')

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Бойко Артур'
printTimeStamp(name)
