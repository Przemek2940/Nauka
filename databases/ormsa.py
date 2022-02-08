#! /home/przemek2940/PycharmProjects/venv00/bin python3
# -*- coding: utf-8 -*-

import os
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

if os.path.exists('test.db'):
    os.remove('test.db')
baza = create_engine('sqlite:///test.db')

BazaModel = declarative_base()

class Klasa(BazaModel):
    __tablename__ = 'klasa'
    id = Column(Integer, primary_key=True)
    nazwa = Column(String(100), nullable=False)
    profil = Column(String(100), default='')
    uczniowie = relationship('Uczen', backref='klasa')


class Uczen(BazaModel):
    __tablename__ = 'uczen'
    id = Column(Integer, primary_key=True)
    imie = Column(String(100), nullable=False)
    nazwisko = Column(String(100), nullable=False)
    klasa_id = Column(Integer, ForeignKey('klasa.id'))

BazaModel.metadata.create_all(baza)

BDSesja = sessionmaker(bind=baza)
sesja = BDSesja()

if not sesja.query(Klasa).count():
    sesja.add(Klasa(nazwa='1A', profil='matematyczny'))
    sesja.add(Klasa(nazwa='1B', profil='humanistyczny'))

inst_klasa = sesja.query(Klasa).filter_by(nazwa='1A').one()

sesja.add_all([
    Uczen(imie='Tomasz', nazwisko='Nowak', klasa_id=inst_klasa.id),
    Uczen(imie='Mariusz', nazwisko='Kowalski', klasa_id=inst_klasa.id),
])

def czytajdane():
    for uczen in sesja.query(Uczen).join(Klasa).all():
        print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)
    print()

czytajdane()