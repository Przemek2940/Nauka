#! /home/przemek2940/PycharmProjects/venv00/bin python3
# -*- coding: utf-8 -*-

import os
from peewee import *

if os.path.exists('test.db'):
    os.remove('test.db')
baza = SqliteDatabase('test.db')

class BazaModel(Model):
    class Meta:
        database = baza


class Klasa(BazaModel):
    nazwa = CharField(null=False)
    profil = CharField(default='')


class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')


baza.connect()
baza.create_tables([Klasa, Uczen])

if Klasa().select().count() == 0:
    inst_klasa = Klasa(nazwa='1A', profil='matematyczny')
    inst_klasa.save()
    inst_klasa=Klasa(nazwa='1B', profil='humanistyczny')
    inst_klasa.save()

inst_klasa = Klasa.select().where(Klasa.nazwa == '1A').get()

uczniowie = [
    {'imie': 'Tomasz', 'nazwisko': 'Nowak', 'klasa': inst_klasa},
    {'imie': 'Mariusz', 'nazwisko': 'Kowalski', 'klasa': inst_klasa}
]

Uczen.insert_many(uczniowie).execute()

def czytajdane():
    for uczen in Uczen.select().join(Klasa):
        print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)
    print()


czytajdane()