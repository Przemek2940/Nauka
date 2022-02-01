#! /home/przemek2940/PycharmProjects/venv00/bin python3
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *

pygame.init()

OKNOGRY_SZER = 800
OKNOGRY_WYS = 400
LT_BLUE = (230, 255, 255)

oknogry = pygame.display.set_mode((OKNOGRY_SZER, OKNOGRY_WYS), 0, 32)

pygame.display.set_caption('Prosty pong')

PALETKA_SZER = 100
PALETKA_WYS = 20
BLUE = (0, 0, 255)
PALETKA_1_POZ = (350, 360)
paletka1 = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
paletka1.fill(BLUE)
paletka1_prost = paletka1.get_rect()
paletka1_prost.x = PALETKA_1_POZ[0]
paletka1_prost.y = PALETKA_1_POZ[1]

P_SZER = 20
P_WYS = 20
P_PREDKOSC_X = 6
P_PREDKOSC_Y = 6
GREEN = (0, 255, 0)
pilka = pygame.Surface([P_SZER, P_WYS], pygame.SRCALPHA, 32).convert_alpha()
pygame.draw.ellipse(pilka, GREEN, [0, 0, P_SZER, P_WYS])
pilka_prost = pilka.get_rect()
pilka_prost.x = OKNOGRY_SZER / 2
pilka_prost.y = OKNOGRY_WYS / 2


#paletka ai
RED = (255, 0, 0)
PALETKA_AI_POZ = (350, 20)
paletkaAI = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
paletkaAI.fill(RED)
paletkaAI_prost = paletkaAI.get_rect()
paletkaAI_prost.x = PALETKA_AI_POZ[0]
paletkaAI_prost.y = PALETKA_AI_POZ[1]
PREDKOSC_AI = 5

#punkty
PKT_1 = '0'
PKT_AI = '0'
fontObj = pygame.font.Font('freesansbold.ttf', 64)


def drukuj_punkty1():
    tekst1 = fontObj.render(PKT_1, True, (0, 0, 0))
    tekst_prost1 = tekst1.get_rect()
    tekst_prost1.center = (OKNOGRY_SZER / 2, OKNOGRY_WYS * 0.75)
    oknogry.blit(tekst1, tekst_prost1)


def drukuj_punktyAI():
    tekstAI = fontObj.render(PKT_AI, True, (0, 0, 0))
    tekst_prostAI = tekstAI.get_rect()
    tekst_prostAI.center = (OKNOGRY_SZER / 2, OKNOGRY_WYS / 4)
    oknogry.blit(tekstAI, tekst_prostAI)


FPS = 30
fpsClock = pygame.time.Clock()
pygame.key.set_repeat(50, 25)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paletka1_prost.x -= 5
                if paletka1_prost.x < 0:
                    paletka1_prost.x = 0
            if event.key == pygame.K_RIGHT:
                paletka1_prost.x += 5
                if paletka1_prost.x > OKNOGRY_SZER - PALETKA_SZER:
                    paletka1_prost.x = OKNOGRY_SZER - PALETKA_SZER

        if event.type == MOUSEMOTION:
            myszaX, myszaY = event.pos
            przesuniecie = myszaX - (PALETKA_SZER / 2)
            if przesuniecie > OKNOGRY_SZER - PALETKA_SZER:
                przesuniecie = OKNOGRY_SZER - PALETKA_SZER
            if przesuniecie < 0:
                przesuniecie = 0
            paletka1_prost.x = przesuniecie
    pilka_prost.move_ip(P_PREDKOSC_X, P_PREDKOSC_Y)

    if pilka_prost.right >= OKNOGRY_SZER:
        P_PREDKOSC_X *= -1
    if pilka_prost.left <= 0:
        P_PREDKOSC_X *= -1
    if pilka_prost.top <= 0:
        pilka_prost.x = OKNOGRY_SZER / 2
        pilka_prost.y = OKNOGRY_WYS / 2
        PKT_1 = str(int(PKT_1) + 1)
    if pilka_prost.bottom >= OKNOGRY_WYS:
        pilka_prost.x = OKNOGRY_SZER / 2
        pilka_prost.y = OKNOGRY_WYS / 2
        PKT_AI = str(int(PKT_AI) + 1)
    if pilka_prost.centerx > paletkaAI_prost.centerx:
        paletkaAI_prost.x += PREDKOSC_AI
    elif pilka_prost.centerx < paletkaAI_prost.centerx:
        paletkaAI_prost.x -= PREDKOSC_AI
    if pilka_prost.colliderect(paletkaAI_prost):
        P_PREDKOSC_Y *= -1
        pilka_prost.top = paletkaAI_prost.bottom
    if pilka_prost.colliderect(paletka1_prost):
        P_PREDKOSC_Y *= -1
        pilka_prost.bottom = paletka1_prost.top

    oknogry.fill(LT_BLUE)
    drukuj_punkty1()
    drukuj_punktyAI()
    oknogry.blit(paletka1, paletka1_prost)
    oknogry.blit(paletkaAI, paletkaAI_prost)
    oknogry.blit(pilka, pilka_prost)
    pygame.display.update()
    fpsClock.tick(FPS)
