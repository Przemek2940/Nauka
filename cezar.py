#! /home/przemek2940/Python/bin python3
# -*- coding: utf-8 -*-
decyzja = input("""Jeśli chcesz zaszyfrować wiadomość - wpisz 1\n
Jeśli chcesz odszyfrować wiadomość - wpisz 2\n""")
KLUCZ = int(input("Jaki ma być klucz?\n"))


def szyfruj(tekst):
    zaszyfrowany = ""
    for znak in tekst:
        if ord(znak) > 90 - KLUCZ and ord(znak) < 97 - KLUCZ:
            zaszyfrowany += chr(ord(znak) + KLUCZ - 26)
        elif ord(znak) > 122 - KLUCZ:
            zaszyfrowany += chr(ord(znak) + KLUCZ - 26)
        else:
            zaszyfrowany += chr(ord(znak) + KLUCZ)
    return zaszyfrowany


def deszyfruj(tekst):
    odszyfrowany = ""
    for znak in tekst:
        if ord(znak) > 122 - KLUCZ:
            odszyfrowany += chr(ord(znak) - KLUCZ + 26)
        else:
            odszyfrowany += chr(ord(znak) - KLUCZ)
    return odszyfrowany


def main(args):
    if decyzja == "1":
        tekst = input("Podaj ciąg do zaszyfrowania:\n")
        print("Ciąg zaszyfrowany:\n", szyfruj(tekst))
    if decyzja == "2":
        tekst = input("Podaj ciąg do odszyfrowania:\n")
        print("Ciąg odszyfrowany:\n", deszyfruj(tekst))



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
