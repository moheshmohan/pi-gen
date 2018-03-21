#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import pygame

time_stamp_prev=0

os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ['SDL_VIDEODRIVER']="fbcon"

def displaytext(text,size,line,color,clearscreen):
    if clearscreen:
        screen.fill((0,0,0))

    font = pygame.font.Font(None,size)
    text = font.render(text,0,color)
    rotated = pygame.transform.rotate(text,90)
    textpos = rotated.get_rect()
    textpos.centery = 80
    if line == 1:
        textpos.centerx = 99
        screen.blit(rotated,textpos)
    elif line == 2:
        textpos.centerx = 61
        screen.blit(rotated,textpos)
    elif line == 3:
        textpos.centerx = 25
        screen.blit(rotated,textpos)

def main():
    global screen

    pygame.init()
    pygame.mouse.set_visible(0)
    size = width,height = 160,128
    screen = pygame.display.set_mode(size)

    while True:
        displaytext(time.strftime("%d.%m.%Y",time.gmtime()),40,1,(255,255,255),True)
        displaytext(time.strftime("%H:%M:%S",time.gmtime()),40,2,(255,255,255),False)
        displaytext("gerfficient.com",20,3,(100,100,255),False)
        pygame.display.flip()
        time.sleep(1)

if __name__ == '__main__':
    main()
