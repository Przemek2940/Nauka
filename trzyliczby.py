#! /home/przemek2940/PycharmProjects/venv00/bin python3
# -*- coding: utf-8 -*-

op = "t"
while op == "t":
    try:
        a, b, c = input("Podaj trzy liczby oddzielone spacjami: ").split(" ")
    except ValueError:
        print("Błąd. Spróbuj jeszcze raz.")
        continue
    print("Wprowadzono liczby:", a, b, c)
    print("\nNajmniejsza: ")

    if a < b:
        if a < c:
            najmniejsza = a
        else:
            najmniejsza = c
    elif b < c:
        najmniejsza = b
    else:
        najmniejsza = c

    print(najmniejsza)

    op = input("Jeszcze raz? t/n")

    print("Koniec")
