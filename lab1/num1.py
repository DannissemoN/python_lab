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
