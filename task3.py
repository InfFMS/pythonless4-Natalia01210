# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C  - 100, D - 500, M - 1000
# Пример:
# 2013
# MMXIII



n = input()
m = []
for i in n:
    m.append(int(i))
m.reverse()
s = ''
if(len(m) > 0):
    t = m[0]
    if(1 <= t and t <= 3):
        s = ('I' * t) + s
    elif(t == 4):
        s = ('IV') + s
    elif(6 <= t and t <= 8):
        s = 'V' + ('I' * (t-5)) + s
    elif(t == 9):
        s = 'IX' + s
if(len(m) > 1):
    t = m[1]
    if (1 <= t and t <= 3):
        s = ('X' * t) + s
    elif (t == 4):
        s = ('XL') + s
    elif (6 <= t and t <= 8):
        s = 'L' + ('X' * (t - 5)) + s
    elif (t == 9):
        s = 'XC' + s
if(len(m) > 2):
    t = m[2]
    if (1 <= t and t <= 3):
        s = ('C' * t) + s
    elif (t == 4):
        s = ('CD') + s
    elif (6 <= t and t <= 8):
        s = 'D' + ('C' * (t - 5)) + s
    elif (t == 9):
        s = 'CM' + s
if(len(m) > 3):
    t = m[3]
    if (1 <= t and t <= 3):
        s = ('M' * t) + s
print(s, end='')