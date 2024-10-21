# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7
def F2(n):
    if(F2 == 1):
        return False
    for i in range(2, int(n**0.5) + 1):
        if(n % i == 0):
            return False
    return True
def F1(n):
    if(F2(n)):
        print(n, end='')
        return ''
    for i in range(2, int(n**0.5)+1):
        if(n % i == 0):
            print(i, '*', sep='', end='')
            F1(n // i)
            return ''

