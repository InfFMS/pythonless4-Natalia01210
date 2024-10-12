# Напишите функцию, которая «переворачивает» число,
# то есть возвращает число, в котором цифры стоят в обратном порядке.
# Вводится натуральное число
# Пользоваться input()[::-1] запрещено!
# Идея задачи реализовать алгоритм,
# который будет работать для любого введенного натурального числа.
def F(n):
    if(n > 9):
        return str(n % 10) + str(F(n // 10))
    return n % 10
n = int(input())
print(F(n))