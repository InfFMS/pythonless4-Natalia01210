# Напишите функцию number_to_words(num), которая принимает
# в качестве аргумента натуральное число num и возвращает
# его словесное описание на русском языке.
#
# Примечание 1.
# Считайте, что число 1 ≤ num ≤ 99.
#
# Примечание 2.
# Следующий программный код:
#
# print(number_to_words(7))
# print(number_to_words(85))
# должен выводить:
#
# семь
# восемьдесят пять

def number_to_words(num):
    res = ''
    a = num // 10
    b = num % 10
    if(a != 0):
        if(a == 9):
            res += "девять"
        elif(a == 8):
            res += "восемь"
        elif (a == 7):
            res += "семь"
        elif (a == 6):
            res += "шесть"
        elif (a == 5):
            res += "пять"
        elif (a == 4):
            res += "сорок "
        elif (a == 3):
            res += "три"
        elif (a == 2):
            res += "два"
        elif(a == 1):
            if (b == 9):
                res += "девятнадцать"
            elif (b == 8):
                res += "восемнадцать"
            elif (b == 7):
                res += "семнадцать"
            elif (b == 6):
                res += "шестнадцать"
            elif (b == 5):
                res += "пятнадцать"
            elif (b == 4):
                res += "четырнадцать"
            elif (b == 3):
                res += "тринадцать"
            elif (b == 2):
                res += "двенадцать"
            elif (b == 1):
                res += "одиннадцать"
            elif(b == 0):
                res += "десять"
            return res
        if(a == 9):
            res = res[:-2] + "носто "
        elif(a > 4):
            res += "десят "
        elif(a == 3 or a == 2):
            res += "дцать "
    if (b == 9):
        res += "девять"
    elif (b == 8):
        res += "восемь"
    elif (b == 7):
        res += "семь"
    elif (b == 6):
        res += "шесть"
    elif (b == 5):
        res += "пять"
    elif (b == 4):
        res += "четыре"
    elif (b == 3):
        res += "три"
    elif (b == 2):
        res += "два"
    elif (b == 1):
        res += "один"
    return res

