#! /home/przemek2940/PycharmProjects/venv00/bin python3
# -*- coding: utf-8 -*-

print(*map(lambda i: 'Fizz' * (not i%3) + 'Buzz' * (not i%5) or i, range(1,101)),sep='\n')