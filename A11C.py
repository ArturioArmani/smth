import datetime
def printTimeStamp(name):
    print('Пікула Руслан Погорілий Артем: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x % y)

print(GCD(15, 5))

