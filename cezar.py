#! /home/przemek2940/PycharmProjects/pythonProject2/venv/bin python3
# -*- coding: utf-8 -*-
decyzja = input("""Jeśli chcesz zaszyfrować wiadomość - wpisz 1\n
Jeśli chcesz odszyfrować wiadomość - wpisz 2\n""")
KLUCZ = int(input("Jaki ma być klucz?\n"))

znaki = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')',      # znaki ktore beda pomijane w szyfrze
         '*', '+', ',', '-', '.', '/', '0', '1', '2', '3',
         '4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
         '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{',
         '|', '}', '~']

def szyfruj(tekst):
    zaszyfrowany = ""
    for znak in tekst:
        if znak in znaki:
            zaszyfrowany += chr(ord(znak))
        elif ord(znak) > 90 - KLUCZ and ord(znak) < 97 - KLUCZ:
            zaszyfrowany += chr(ord(znak) + KLUCZ - 26)
        elif ord(znak) > 122 - KLUCZ:
            zaszyfrowany += chr(ord(znak) + KLUCZ - 26)
        else:
            zaszyfrowany += chr(ord(znak) + KLUCZ)
    return zaszyfrowany


def deszyfruj(tekst):
    odszyfrowany = ""
    KLUCZM = KLUCZ % 26
    for znak in tekst:
        if znak in znaki:
            odszyfrowany += chr(ord(znak))
        elif (ord(znak) - KLUCZM < 65):
            odszyfrowany += chr(ord(znak) - KLUCZM + 26)
        elif (ord(znak) - KLUCZM < 97) and (ord(znak) - KLUCZM > 90):
            odszyfrowany += chr(ord(znak) - KLUCZM + 26)
        else:
            odszyfrowany += chr(ord(znak) - KLUCZM)
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
