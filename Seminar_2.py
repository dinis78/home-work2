import os
from unicodedata import name
os.system("cls")

#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#6782 -> 23
#0,56 -> 11

# number=(input('Введите число '))
# str_number=str(number)                       #преобразовываем в строку
# str_number=str_number.replace('.', '')       #убираем разделитель
# list_number=list(str_number)                 #преобразовыаем строку в список чисел
# list_num=map(int, list_number)               #делем целые числа
# print(sum(list_num))                         #складываем числа
#####################################################

#Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

x=int(input('Введите число '))
i=0
while i<x:
    def fact(i):
        if i==1:
            return 1
        else:
            return i*fact(i-1)
    i+=1
    str_fact=str(fact(i))
    print(str_fact, sep=',', end='')




