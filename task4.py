# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.
a, b = int(input()), int(input())
for i in range(min(a, b), 0, -1):
    if(a % i == 0 and b % i == 0):
        print("НОД:", i)
        exit()
