import math 
IMT = int(input("Розрахунок відбуватиметься в: \n[1]Дюймах та фунтах\n[2]Метрах та кілограмах\n"))
a = float(input("Ваш зріст(в метрах) :"))
b = int(input("Ваша вага :"))
if IMT == 1:
  IMT = b / math.pow(a,2) * 703
if IMT == 2:
  IMT = float(b / math.pow(a,2))
print ('Ваш ІМТ:','=',IMT) 

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Бойко Артур'
printTimeStamp(name)
