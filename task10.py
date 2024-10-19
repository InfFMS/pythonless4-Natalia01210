# Напишите функцию convert_base(num, from_base, to_base),
# которая переводит натуральное число num из системы
# счисления с основанием from_base в систему счисления
# с основанием to_base
# 2 ≤ to_base ≤ 36 ; 2 ≤ from_base ≤ 36
# На входе три числа num, from_base, to_base
# На выходе одно число - результат работы функции
# Подсказка (если не получается решить):
# Попробуйте разбить задачу на две подзадачи:
# перевод из десятичной системы счисления в любую
# перевод из любой системы счисления в десятичную
# Объедините эти две подзадачи, получите ответ.
def F(a, n):
    sum = 0
    m = []
    for i in a:
        m.append(i)
    k = len(m) - 1
    for i in m:
        if(ord('0') <= ord(i) and ord(i) <= ord('9')):
            sum += int(i) * n ** k
            k -= 1
            continue
        else:
            t = ord(i) - ord('A') + 10
            sum += t * n ** k
            k -= 1
    return sum

def F2(a, n):
    sum = ''
    while(a > 0):
        t = a % n
        if(0 <= t and t <= 9):
            sum = str(t) + sum
        else:
            sum = chr(ord('A') + t - 10) + sum
        a //= to_base
    return sum




num, from_base, to_base = input(), int(input()), int(input())
x = F(num, from_base)
print(F2(x, to_base))

