#! /home/przemek2940/Python/bin/ python3
# -*- coding: utf-8 -*-

# informacje python
aktrok = int(input("Który mamy teraz rok? "))
rokpythona = 1989
wiekpythona = aktrok - rokpythona

# informacje o użytkownia
imie = input("Podaj imię ")
wiek = int(input("Podaj wiek "))
roznica = abs(wiekpythona - wiek)
# komunikat
print("Mów mi Python. Mam", wiekpythona, "lat. Witaj w moim świecie " + str(imie) + ".")

#instrukcja warunkowa
if wiekpythona < wiek:
    print("Jesteś starszy ode mnie o " + str(roznica) + " lat.")

if wiekpythona > wiek:
    print("Jesteś młodszy ode mnie o " + str(roznica) + " lat.")

if wiekpythona == wiek:
    print("Jesteśmy rówieśnikami.")