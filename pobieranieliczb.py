#! /home/przemek2940/PycharmProjects/pythonProject2/venv/bin python3
# -*- coding: utf-8 -*-

from random import randint

ile = int(input("Ile liczb wylosować? "))
lista = []

for i in range(0, ile):
    lista.append(randint(0, 100))
print(lista)

print("Dodawanie trzech elementów na końcu listy")
for i in range(0, 3):
    if i == 0:
        liczba = int(input("Podaj pierwszą liczbę: "))
        lista.append(liczba)
        print(lista)
    if i == 1:
        liczba = int(input("Podaj drugą liczbę: "))
        lista.append(liczba)
        print(lista)
    if i == 2:
        liczba = int(input("Podaj trzecią liczbę: "))
        lista.append(liczba)
        print(lista)

print("Zawartość listy ([indeks] wartość):")
for i, v in enumerate(lista):
    print("[", i, "]", v)

print("Elementy w odwróconej kolejności:")
for e in reversed(lista):
    print(e, end=" ")

print()
print("Elementy posortowane rosnąco:")
for e in sorted(lista):
    print (e, end=" ")

print()
e = int(input("Którą liczbę usunąć? "))
lista.remove(e)
print(lista)

print("Wstawianie elementów do listy")
a, i = eval(input("Podaj element i indeks oddzielone przecinkiem: "))
lista.insert(i, a)
print(lista)

print("Wyszukiwanie i zliczanie elementu w liście")
e = int(input("Podaj liczbę: "))
print("Liczba wystąpień: ")
print(lista.count(e))
print("Indeks pierwszego wystąpienia: ")
if lista.count(e):
    print(lista.index(e))
else:
    print("Brak elementu w liście")

print("Pobieramy ostatni element z listy: ")
print(lista.pop())
print(lista)

print("Część listy (notacja wycinkowa):")
i, j = eval(input("Podaj indeks początkowy i końcowy oddzielone przecinkiem "))
print(lista[i:j])

