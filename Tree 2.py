from pygame import *
from math import *
from random import *
#####################################
screen=display.set_mode((1000,800)) #
running=True                        #
#####################################
def treeDraw(startx,starty,lenght,branches,changex):
    for i in range(0,branches):
        endx=startx
        endy=starty-lenght
        draw.line(screen,(255,255,255),(startx,starty),(endx+20,endy))
        draw.line(screen,(255,255,255),(startx,starty),(endx-20,endy))
        draw.line(screen,(255,255,255),(startx,starty),(endx,endy))
        if lenght>5:
            treeDraw(endx,endy,lenght//2,3,changex)
        else:
            return
    return
    
while running:
    clock=time.Clock()
    clock.tick(100)
    #screen.fill((0,0,0))
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            treeDraw(mx,my,100,1,20)
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys=key.get_pressed()
    #####################################################
    '''if 1 in mb:
        treeDraw(mx,my,100,3)'''
    display.flip()
quit()
