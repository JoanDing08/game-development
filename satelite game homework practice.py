#use different images and a 10/15 second countdown

import pgzrun
from random import randint
WIDTH=600
HEIGHT=600
planets=[]
lines=[]
ttl_sats=10
current_sat=0
gameover=False
def make_planets():
    global st_time,planets
    for i in range(ttl_sats):
        img=Actor("planet")
        img.pos=randint(50,500),randint(50,500)
        planets.append(img)
    

def draw():
    screen.blit("space",(0,0))
    num=1
    for i in planets:
        screen.draw.text(str(num),(i.pos[0],i.pos[1]+20))
        i.draw()
        num+=1
    for i in lines:
        screen.draw.line(i[0],i[1],"white")
    if gameover:
        screen.fill("black")
        screen.draw.text("The time is up!",topright=(470,250),fontsize=70)


def timer():
    global gameover
    gameover=True
clock.schedule(timer,15)

make_planets()

def on_mouse_down(pos):
    global current_sat,ttl_sats,planets,lines
    if current_sat<ttl_sats:
        if planets[current_sat].collidepoint(pos):
            if planets:
                lines.append((planets[current_sat-1].pos,planets[current_sat].pos))
            current_sat+=1
        else:
            current_sat=0
            lines=[]


pgzrun.go()