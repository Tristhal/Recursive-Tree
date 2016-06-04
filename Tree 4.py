from pygame import *
from math import *
from random import *
#####################################
screen=display.set_mode((1000,800)) #
running=True                        #
#####################################
'''def treeDraw(startx,starty,lenght,branches):
    for i in range(0,branches):
        endx=startx+randint(-40,40)
        endy=starty-lenght
        draw.line(screen,(255,255,255),(startx,starty),(endx,endy))
        if lenght>5:
            treeDraw(endx,endy,lenght//choice([1.3,1.7,2]),3)
            treeDraw(endx,endy,lenght-randint(5,20),3)
        else:
            if randint(0,20)==1:
                draw.circle(screen,(200,50,50),(int(endx),int(endy)),5)
            return
    return'''
def treeDraw(startx,starty,lenght,branches):
    for i in range(0,branches):
        endx=startx+randint(-40,40)
        endy=starty-lenght
        draw.line(screen,(255,255,255),(startx,starty),(endx,endy))
        if lenght>5:
            treeDraw(endx,endy,lenght//choice([1.3,1.7,2]),3)
            treeDraw(endx,endy,lenght-randint(5,20),3)
        else:
           if randint(0,20)==1:
                draw.circle(screen,(200,50,50),(int(endx),int(endy)),5)
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
            treeDraw(mx,my,100,1)
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys=key.get_pressed()
    #####################################################
    '''if 1 in mb:
        treeDraw(mx,my,100,3)'''
    display.flip()
quit()
