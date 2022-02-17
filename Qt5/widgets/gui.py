# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from ksztalt import Ksztalty, Ksztalt
from PyQt5.QtWidgets import QHBoxLayout, QCheckBox, QButtonGroup, QVBoxLayout, QSlider, QLCDNumber, QSplitter
from PyQt5.QtWidgets import QRadioButton, QGroupBox, QComboBox, QSpinBox, QPushButton, QLabel, QLineEdit
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

        # Lista Combobox i spinbox
        self.listaRGB = QComboBox(self)
        for v in ('R', 'G', 'B'):
            self.listaRGB.addItem(v)
        self.listaRGB.setEnabled(False)
        #spinbox
        self.spinRGB = QSpinBox()
        self.spinRGB.setMinimum(0)
        self.spinRGB.setMaximum(255)
        self.spinRGB.setEnabled(False)

        uklad = QVBoxLayout()
        uklad.addWidget(self.listaRGB)
        uklad.addWidget(self.spinRGB)
        ukladH3.insertSpacing(1, 25)
        ukladH3.addLayout(uklad)

        #przyciski PushButton
        uklad = QHBoxLayout()
        self.grupaP = QButtonGroup()
        self.grupaP.setExclusive(False)
        for v in ('R', 'G', 'B'):
            self.btn = QPushButton(v)
            self.btn.setCheckable(True)
            self.grupaP.addButton(self.btn)
            uklad.addWidget(self.btn)

        self.grupaPBtn = QGroupBox('Przyciski RGB')
        self.grupaPBtn.setLayout(uklad)
        self.grupaPBtn.setObjectName('Push')
        self.grupaPBtn.setCheckable(True)
        self.grupaPBtn.setChecked(False)

        #etykiety QLabel i pola QLineEdit
        ukladH4 = QHBoxLayout()
        self.labelR = QLabel('R')
        self.labelG = QLabel('G')
        self.labelB = QLabel('B')
        self.kolorR = QLineEdit('0')
        self.kolorG = QLineEdit('0')
        self.kolorB = QLineEdit('0')
        for v in ('R', 'G', 'B'):
            label = getattr(self, 'label' + v)
            kolor = getattr(self, 'kolor' + v)
            ukladH4.addWidget(label)
            ukladH4.addWidget(kolor)
            kolor.setMaxLength(3)

        ukladOkna = QVBoxLayout()
        ukladOkna.addLayout(ukladH1)
        ukladOkna.addWidget(ukladH2)
        ukladOkna.addLayout(ukladH3)
        ukladOkna.addWidget(self.grupaPBtn)
        ukladOkna.addLayout(ukladH4)
        self.setLayout(ukladOkna)
        self.setWindowTitle('Widżety')