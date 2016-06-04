from pygame import *
from math import *
from random import *
#####################################
screen=display.set_mode((1000,800)) #
running=True                        #
#####################################
def treeDraw(startx,starty,lenght,branches):
    for i in range(0,branches):
        endx=startx-randint(-30,30)
        endy=starty-lenght-randint(-5,5)
        draw.line(screen,(255,255,255),(startx,starty),(endx,endy))
        if lenght>5:
            treeDraw(endx,endy,lenght-randint(5,50),3)
        else:
            return
    
while running:
    clock=time.Clock()
    clock.tick(100)
    #screen.fill((0,0,0))
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            treeDraw(mx,my,100,1)
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys=key.get_pressed()
    #####################################################
    '''if 1 in mb:
        treeDraw(mx,my,100,3)'''
    display.flip()
quit()
