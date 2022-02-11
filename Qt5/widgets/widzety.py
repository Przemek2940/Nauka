#! /home/przemek2940/PycharmProjects/venv00/bin python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from gui import Ui_Widget
from PyQt5.QtGui import QColor

class Widgety(QWidget, Ui_Widget):

    kanaly = {'R'}
    kolorW = QColor(0, 0, 0)
    def __init__(self, parent=None):
        super(Widgety, self).__init__(parent)
        self.setupUi(self)

        self.grupaChk.buttonClicked[int].connect(self.ustawKsztalt)
        self.ksztaltChk.clicked.connect(self.aktywujKsztalt)
        for i in range(self.ukladR.count()):
            self.ukladR.itemAt(i).widget().toggled.connect(self.ustawKanalRbtn)
        self.suwak.valueChanged.connect(self.zmienKolor)

    def ustawKanalRbtn(self, wartosc):
        self.kanaly = set()
        nadawca = self.sender()
        if wartosc:
            self.kanaly.add(nadawca.text())

    def zmienKolor(self, wartosc):
        self.lcd.display(wartosc)
        if 'R' in self.kanaly:
            self.kolorW.setRed(wartosc)
        if 'G' in self.kanaly:
            self.kolorW.setGreen(wartosc)
        if 'B' in self.kanaly:
            self.kolorW.setBlue(wartosc)

        self.ksztaltAktywny.ustawKolorW(
            self.kolorW.red(),
            self.kolorW.green(),
            self.kolorW.blue())

    def ustawKsztalt(self, wartosc):
        self.ksztaltAktywny.ustawKsztalt(wartosc)

    def aktywujKsztalt(self, wartosc):
        nadawca = self.sender()
        if wartosc:
            self.ksztaltAktywny = self.ksztalt1
            nadawca.setText('<=')
        else:
            self.ksztaltAktywny = self.ksztalt2
            nadawca.setText('=>')
        self.grupaChk.buttons()[self.ksztaltAktywny.ksztalt].setChecked(True)
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Widgety()
    okno.show()

    sys.exit(app.exec_())