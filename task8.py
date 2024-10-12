# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7
def F(n):
    res = ''
    for i in range(2, int(n ** 0.5) + 1):
        while (n % i == 0):
            res += str(i)
            res += '*'
            n /= i
    if(n != 1):
        res += str(int(n))
        res += '*'
    return res[:-1]
n = int(input())
print(F(n))

