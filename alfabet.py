#! /home/przemek2940/PycharmProjects/pythonProject2/venv/bin python3
# -*- coding: utf-8 -*-

n = int(input("Podaj co którą literę chcesz ujrzeć: "))
print("Alfabet w porządku naturalnym:")
x = 0
for i in range(65, 91, n):
    litera = chr(i)
    x += 1
    tmp = litera + " => " + litera.lower()
    if x == 5:
        x = 0
        print("\n", end=" ")
    print(tmp, end=" ")

x = -1
print("\nAlfabet w porządku odwróconym:")
for i in range(122, 96, -n):
    litera = chr(i)
    x += 1
    if x == 5:
        x = 0
        print("\n", end=" ")
    print(litera.upper(), "=>", litera, end=" ")