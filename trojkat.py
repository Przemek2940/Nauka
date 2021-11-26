#! /home/przemek2940/Python/bin python3
# -*- coding: utf-8 -*-

import math

op = "t"
while op != "n":
    dane = input("Podaj 3 boki trójkąta (oddzielone przecinkami): ")

    lista = []
    for x in dane.split(","):
        lista.append(int(x))
    a, b, c = lista

    print("Podano boki: ", a, b, c)

    if a + b > c and a + c > b and b + c > a:
        print("Z podanych boków można zbudować trójkąt.")
        if (a**2 + b**2 == c**2 or
                a**2 + c**2 == b**2 or
                b**2 + c**2 == a**2):
            print("Jest to trójkąt prostokątny.")
        print("Jego obwód wynosi:", (a + b + c))
        p = 0.5 * (a + b + c)
        # Wzór Herona na pole trójkąta
        P = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Pole wynosi:", P)
        op = "n"
    else:
        print("Z podanych długości boków nie można utworzyć trójkąta.")
        op = input("Spróbujesz jeszcze raz? (t/n:) ")
