# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from ksztalt import Ksztalty, Ksztalt
from PyQt5.QtWidgets import QHBoxLayout, QCheckBox, QButtonGroup, QVBoxLayout, QSlider, QLCDNumber, QSplitter
from PyQt5.QtWidgets import QRadioButton, QGroupBox
from PyQt5.QtCore import Qt


class Ui_Widget(object):

    def setupUi(self, Widget):
        self.ksztalt1 = Ksztalt(self, Ksztalty.Polygon)
        self.ksztalt2 = Ksztalt(self, Ksztalty.Ellipse)
        self.ksztaltAktywny = self.ksztalt1

        #przyciski
        uklad = QVBoxLayout()
        self.grupaChk = QButtonGroup()
        for i, v in enumerate(('Kwadrat', 'Koło', 'Trójkąt', 'Linia')):
            self.chk = QCheckBox(v)
            self.grupaChk.addButton(self.chk, i)
            uklad.addWidget(self.chk)
        self.grupaChk.buttons()[self.ksztaltAktywny.ksztalt].setChecked(True)
        self.ksztaltChk = QCheckBox('<=')
        self.ksztaltChk.setChecked(True)
        uklad.addWidget(self.ksztaltChk)

        ukladH1 = QHBoxLayout()
        ukladH1.addWidget(self.ksztalt1)
        ukladH1.addLayout(uklad)
        ukladH1.addWidget(self.ksztalt2)

        #slider, lcdnumber
        self.suwak = QSlider(Qt.Horizontal)
        self.suwak.setMinimum(0)
        self.suwak.setMaximum(255)
        self.lcd = QLCDNumber()
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        ukladH2 = QSplitter(Qt.Horizontal, self)
        ukladH2.addWidget(self.suwak)
        ukladH2.addWidget(self.lcd)
        ukladH2.setSizes((125,75))

        #RadioButton
        self.ukladR = QHBoxLayout()
        for v in ('R', 'G', 'B'):
            self.radio = QRadioButton(v)
            self.ukladR.addWidget(self.radio)
        self.ukladR.itemAt(0).widget().setChecked(True)

        self.grupaRBtn = QGroupBox('Opcje RGB')
        self.grupaRBtn.setLayout(self.ukladR)
        self.grupaRBtn.setObjectName('Radio')
        self.grupaRBtn.setCheckable(True)
        ukladH3 = QHBoxLayout()
        ukladH3.addWidget(self.grupaRBtn)

        ukladOkna = QVBoxLayout()
        ukladOkna.addLayout(ukladH1)
        ukladOkna.addWidget(ukladH2)
        ukladOkna.addLayout(ukladH3)

        self.setLayout(ukladOkna)
        self.setWindowTitle('Widżety')