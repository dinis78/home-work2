from asyncore import write
from datetime import date
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
# print(sum(list_num))                        
#####################################################

#Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# x=int(input('Введите число '))
# i=0
# while i<x:
#     def fact(i):
#         if i==1:
#             return 1
#         else:
#             return i*fact(i-1)
#     i+=1
#     str_fact=str(fact(i))
#     print(str_fact, sep=',', end='')


##############################################################

#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#Пример:Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
#Задайте список из n чисел последовательности (1 + 1/n)**n
# и выведите на экран их сумму.



# n = int(input("Введите число: "))
# def generate_list(n):
#     result = []
#     for i in range(1, n+1):
#         result.append(round((1 + 1/i)**i))
#     return result
# number_list = generate_list(n)
# print(f"Для n = {n}: {number_list} -> {sum(number_list)}")
##############################################

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение
#элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# x=['2', '5']
# data=open('file.txt', 'w')
# data.write('3 \n')
# data.write('5')
# data.close()



size=int(input('Введите число '))
num_list=list(range(-size, size+1))
path='file.txt'
data=open(path, 'r')
rez=1
for position in data:
    rez*=num_list[int(position)]
    data.close()
    print(num_list)
    print(rez)

















#Реализуйте алгоритм перемешивания списка.

# lst = [1, 2, 3, 4, 5]
# print ('Исходный список :', lst)

# for i in range(len(lst)-1, 0, -1):
#     j = random.randint(0, i + 1) # Берем случайный индекс от 0 до i
#     lst[i], lst[j] = lst[j], lst[i] # Меняем arr[i] с элементом случайеого индекса

# print ('перемешаный список : ', lst)