from pygame import *
from math import *
from random import *
import os
#####################################
screen=display.set_mode((1000,800)) #
running=True                        #
#####################################
###
def treeDraw(startx,starty,lenght,branches,variantx):
    for i in range(0,branches):
        variantx+=choice([-2,5,-3,5,7,-2,2,-6,0,-2,3,-3])
        endx=startx+variantx
        endy=starty-lenght
        draw.line(screen,(255,255,255),(startx,starty),(endx,endy))
        if lenght>5:
            treeDraw2(endx,endy,lenght//choice([1.3,1.7,2,1.3,1.7,2,1.3,1.7,2,.99]),3,variantx)
        else:
            if randint(0,20)==1:
                draw.circle(screen,(200,50,50),(int(endx),int(endy)),5)
            return
    return
def treeDraw2(startx,starty,lenght,branches,variantx):
    for i in range(0,branches):
        endx=startx+randint(-30,30)+variantx
        endy=starty-lenght
        draw.line(screen,(255,255,255),(startx,starty),(endx,endy))
        if randint(0,8)==1:
            return
        if lenght>5:
            treeDraw2(endx,endy,lenght//choice([1.3,1.7,2,1.3,1.7,2,1.3,1.7,2,.98]),3,variantx)
        else:
            if randint(0,20)==1:
                draw.circle(screen,(200,50,50),(int(endx),int(endy)),5)
            return
    return
    
while running:
    clock=time.Clock()
    clock.tick(100)
    mx, my = mouse.get_pos()
    #screen.fill((0,0,0))
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            treeDraw(mx,my,100,1,0)
    mb = mouse.get_pressed()
    keys=key.get_pressed()
    #####################################################
    '''if 1 in mb:
        treeDraw(mx,my,100,3)'''
    display.flip()
quit()
