#! /home/przemek2940/PycharmProjects/pythonProject2/venv/bin python3
# -*- coding: utf-8 -*-

import os # isfile
import csv

slownik = {}
sPlik = "slownik.txt"


def otworz(plik):
    if os.path.isfile(sPlik):
        with open(sPlik, newline='') as plikcsv:
            tresc = csv.reader(plikcsv)
            for linia in tresc:
                slownik[linia[0]] = linia[1:]
                return len(slownik)


def zapisz(slownik):
    with open(sPlik, "w", newline='') as plikcsv:
        tresc = csv.writer(plikcsv)
        for wobcy in slownik:
            lista = slownik[wobcy]
            lista.insert(0, wobcy)
            tresc.writerow(lista)


def oczysc(str):
    str = str.strip()
    str = str.lower()
    return str


def main(args):
    print("""Podaj dane w formacie: wyraz obcy: znaczenie1, znaczenie2
    Aby zakończyć wprowadzanie danych, podaj 0.""")

    # wobce = set()
    nowy = False
    ileWyrazow = otworz(sPlik)
    print("Wpisów w bazie:", ileWyrazow)

    #glówna pętla
    while True:
        dane = input("Podaj dane: ")
        t = dane.split(":")
        wobcy = t[0].strip().lower()
        if wobcy == '0':
            break
        elif dane.count(":") == 1:
            if wobcy in slownik:
                print("Wyraz", wobcy, " i jego znaczenia są już w słowniku.")
                op = input("Zastąpić wpis (t/n)? ")
            if wobcy not in slownik or op == "t":
                znaczenia = t[1].split(",")
                znaczenia = list(map(oczysc, znaczenia))
                slownik[wobcy] = znaczenia
                nowy = True
        else:
                print("Błędny format.")

    if nowy:
        zapisz(slownik)

    print(slownik)

    print("=" * 50)
    print("{0: <15}{1: <40}".format("Wyraz obcy", "Znaczenia"))
    print("=" * 50)
    for wobcy in slownik:
        print("{0: <15}{1: <40}".format(wobcy, ",".join(slownik[wobcy])))


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))