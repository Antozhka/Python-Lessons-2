#Теорема Пифагора
print('Введите катет 1')
a = float(input())
print('Введите катет 2')
b = float(input())
from math import sqrt
c = sqrt(a * a + b * b)
print('Гипотенуза равна {}'.format(c))

#Пятизначное число
print('Введите пятизначное число')
a = int(input())
b = str(a)
for i in range(len(b)):
    print('{0} цифра равна {1}'.format(i + 1, b[i]))

#Сортировка
arr = [0, 3, 24, 2, 5, 7]
for i in range(len(arr)-1):
    x = arr[i]
    n = i
    for j in range(i+1, len(arr)):
        if x > arr[j]:
            x = arr[j]
            n = j
    if n != i:
        arr[i], arr[n] = arr[n], arr[i]
print(arr)