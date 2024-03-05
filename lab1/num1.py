#Функция 1 Найти количество делителей числа, не делящихся на 3
a = int(input())  

def func1(x):
    k = 0
    i = 1
    while x > i:
        if (x%i == 0) and (i%3 != 0 ):
            k+=1
        i+=1

    return k

print(func1(a))


# функция 2 Найти минимальную нечетную цифру числа.
a = int(input())  

min = 9
def func2(x, m2):
    while x%10 > 0:
        if ((x%10) < m2) and (x%2 != 0):
            m2 = x%10
        x = x//10
    return m2

print(func2(a,min))
