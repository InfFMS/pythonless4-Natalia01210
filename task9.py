# Дано натуральное число N. Выведите слово YES,
# если число N является точной степенью двойки,
# или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
# Задача на рекурсию!
def F(n):
    if (n == 1):
        return True
    if(n % 2 == 1):
        return False
    return F(n / 2)
N = int(input())
if(F(N)):
    print("YES")
else:
    print("NO")