import datetime
def printTimeStamp(name):
    print('Пікула Руслан Погорілий Артем: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

baks = int(input("Vasha zdacha: "))
nominals = [2,1,5,10,50]

nominals.sort()
nominals.reverse()
summ = 0
print (baks, '$ =>')

for k in nominals:
    d = baks//k
    baks = baks -d*k
    print (k,'$ :',int(d))
    summ += d

print ('V summe:', summ)


