#! /home/przemek2940/PycharmProjects/venv00/bin python3
# -*- coding: utf-8 -*-

import pylab

a = 1
b = 2
x = range (-10, 11)

y = []
for i in x:
    y.append(a * i + b)

pylab.plot(x, y)
pylab.title('Wykres f(x) = a*x -b')
pylab.grid(True)
pylab.show()
