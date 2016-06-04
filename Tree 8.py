from pygame import *
from math import *
from random import *
#####################################
screen=display.set_mode((1000,800)) #
running=True                        #
#####################################
###
def treeDraw(startx,starty,lenght,branches,variantx):
    for i in range(0,branches):
        variantx-=30
        changey=sin(radians(270+variantx))*lenght
        changex=cos(radians(270+variantx))*lenght
        endx=startx+changex
        endy=starty+changey
        draw.circle(screen,(200,50,50),(int(endx),int(endy)),2)
        draw.line(screen,(255,255,255),(startx,starty),(endx,endy))
        if lenght>5:
            treeDraw(endx,endy,lenght//2,3,variantx)
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
