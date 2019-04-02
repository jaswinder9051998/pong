import pygame
import random
import math
pygame.init()
WIDTH=800
WIDTHGAME=400
HEIGHT=400
WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)
GREEN=(0,255,0)
BOUN=(165,42,42)
game_display=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blob World")
clock=pygame.time.Clock()

class Blob:
    def __init__(self,color):
        self.color=color
        self.x=(int)(WIDTHGAME/2)
        self.size=random.randrange(4,8)
        self.y=self.size+10#(int)(HEIGHT-self.size)
        self.dir=225

    def move(self,xinc=0,yinc=0):
        self.move_x=xinc
        self.y+=yinc
        self.x+=self.move_x
        if(self.x<0):
            self.x=WIDTH
        if(self.x>WIDTH):
            self.x=0
        if(self.y+self.size>=HEIGHT):
            if(self.dir>=270):
                self.dir=360-self.dir
            elif(self.dir>180 and self.dir<270):
                self.dir=360-self.dir
            #self.y=HEIGHT-self.size
        if(self.y-self.size<=0):
            if(self.dir<=90):
                self.dir=360-self.dir
            elif(self.dir>90):
                self.dir=360-self.dir
            #self.y=0

    def check(self,p1,p2):
        if((self.x-self.size)<=(p1.x+p1.width) and (self.y>=p1.y and self.y<=(p1.y+p1.height))):
            if(self.dir<=180):
                self.dir=180-self.dir
            elif(self.dir>180 and self.dir<270):
                self.dir=360+180-self.dir
        elif((self.x+self.size)>=(p2.x) and (self.y>=p2.y and self.y<=(p2.y+p2.height))):
            if(self.dir<=90):
                self.dir=180-self.dir
            elif(self.dir>270):
                self.dir=180+360-self.dir
        
    
    
class Paddle1:
    def __init__(self,color):
        self.color=color
        self.x=0
        self.y=(int)(HEIGHT/2)
        self.width=10
        self.height=80
    def move(self,yinc):
        self.y+=yinc
        if(self.y+self.height>HEIGHT):
            self.y=HEIGHT-self.height
        elif(self.y<0):
            self.y=0
class Paddle2:
    def __init__(self,color):
        self.color=color
        self.y=0
        self.width=10
        self.x=WIDTH-self.width
        self.height=80
    def move(self,yinc):
        self.y+=yinc
        if(self.y+self.height>HEIGHT):
            self.y=HEIGHT-self.height
        elif(self.y<0):
            self.y=0   

      
def draw_enviroment(blob,paddle1,paddle2):
  game_display.fill(WHITE)
  pygame.draw.line(game_display,BOUN,(400,0),(400,400))
  pygame.draw.circle(game_display,blob.color,[(int)(blob.x),(int)(blob.y)],blob.size)
  pygame.draw.rect(game_display,paddle1.color,[paddle1.x,paddle1.y,paddle1.width,paddle1.height])
  pygame.draw.rect(game_display,paddle2.color,[paddle2.x,paddle2.y,paddle2.width,paddle2.height])
  pygame.display.update()
  #blob.move()
  
def main():
    red_blob=Blob(color=RED)
    paddle1=Paddle1(color=BLUE)
    paddle2=Paddle2(color=BLUE)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        key=pygame.key.get_pressed()
        if key[pygame.K_UP]:
            paddle1.move(-5)
        if key[pygame.K_DOWN]:
            paddle1.move(+5)
        if key[pygame.K_w]:
            paddle2.move(-5)
        if key[pygame.K_s]:
            paddle2.move(+5)
        red_blob.check(paddle1,paddle2)
        red_blob.move(math.cos(math.pi *red_blob.dir/180)*3,-math.sin(math.pi*red_blob.dir/180)*3)
        
            

                
        draw_enviroment(red_blob,paddle1,paddle2)
        clock.tick(60)

    
if __name__=='__main__':
  main()
