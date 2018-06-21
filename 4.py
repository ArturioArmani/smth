letter = input("Введіть букву англійського алфавіту :")
golosni =['a','e','u','o','i']
if letter in golosni :
 print ('Голосна')
elif letter == 'y' :
 print ('Інколи голосна,інколи - приголосна')
else :
 print ('Приголосна')

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Бойко Артур'
printTimeStamp(name)

