import pygame

pygame.mixer.pre_init(44100, 16, 2, 4096)

pygame.init() #ine time at the beginning

win=pygame.display.set_mode((500,480)) #creating a window called win

pygame.display.set_caption("First Game") #giving our program a proper name

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

#Caracter Move ==>
clock=pygame.time.Clock()

bulletSound=pygame.mixer.Sound('bullet.wav')
hitSound=pygame.mixer.Sound('hit.wav')
music=pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1) #play music all the game 

score=0
class player(object):

       def __init__(self,x,y,width,height):
           self.x=x
           self.y=y
           self.width=width
           self.height=height
           self.vel=5
           self.isJump=False
           self.jumpVel=10
           self.left=False
           self.right=False
           self.walkCount=0
           self.standing=True
           self.hitbox=(self.x+17,self.y+11,29,52)

           
       def draw(self,win):
           if self.walkCount+1>=27:
             self.walkCount=0
           if not(self.standing):
              if self.left:
               win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
               self.walkCount+=1
              elif self.right:
                win.blit(walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
           else:
                  if self.right:              
                      win.blit(walkRight[0],(self.x,self.y))
                  else:
                     win.blit(walkLeft[0],(self.x,self.y))
           self.hitbox=(self.x+20,self.y,28,60)
           #pygame.draw.rect(win,(255,0,0),self.hitbox,2)         
       def hit(self,enemy):
         self.x=60
         self.y=410
         enemy.y=410
         enemy.x=400
         self.walkCount=0
         font1=pygame.font.SysFont('comicsans',100)
         text=font1.render('-5',1,(255,0,0))
         win.blit(text,(250-(text.get_width()/2),200))
         pygame.display.update()
         i=0
         while i<100:
                pygame.time.delay(10)
                i+=1
                for event in pygame.event.get():
                       if event.type==pygame.QUIT:
                              i=301
                              pygame.quit()
                


"""x=50
y=400
width=64
height=64
vel=4 #velocity #vitesse
isJump=False
value=9
jumpVel=value
left = False
right = False
walkCount=0
"""
class projectile(object):
       def __init__(self,x,y,radius,color,facing):
           self.x=x
           self.y=y
           self.color=color
           self.radius=radius
           self.facing=facing
           self.vel=8*facing
       def draw(self,win):
              
            pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

class enemy(object):
      walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
      walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
      def __init__(self,x,y,width,height,end):
              self.x=x
              self.y=y
              self.width=width
              self.height=height
              self.end=end
              self.walkCount=0
              self.vel=3
              self.hitbox=(self.x+17,self.y+2,31,57)
              self.health=10
              self.visible=True
      def draw(self,win):
             if self.visible:
                     self.move()
                     if self.walkCount+1>=33:
                         self.walkCount=0
                     if self.vel>0:
                         win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
                         self.walkCount+=1
                     else:
                         win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
                         self.walkCount+=1
                     pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,50,10))
                     pygame.draw.rect(win,(0,128,0),(self.hitbox[0],self.hitbox[1]-20,50-(5*(10-self.health)),10))
                     self.hitbox=(self.x+17,self.y+2,31,57)
                     #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
              
      def hit(self):
             if self.health>0:
                    self.health-=1
             else:
                 self.visible=False
                     
             print('hit')
             hitSound.play()
                      
               
      def move(self):
                 if self.vel>0:
                      if self.x+self.vel<500:
                             self.x+=self.vel
                      else:
                              self.vel=self.vel*-1
                              self.welkCount=0
                 else:
                       if self.x-self.vel>0:
                              self.x+=self.vel
                       else:
                              self.vel=self.vel*-1
                              self.welkCount=0       
              

              
def redrawGameWindow():
    win.blit(bg,(0,0))
    text=font.render('score : '+str(score),1,(180,0,0))
    win.blit(text,(390,10))
    #drawing the character ==>
    #pygame.draw.rect(win,(128,181,240),(x,y,width,height))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


font=pygame.font.SysFont('Score :',20,True)     
man=player(400,410,64,64)
goblin=enemy(100,410,64,64,450)
bullets=[]
run = True #run variable
while run : #to check for collisions
    #pygame.time.delay(100) #the clock of the game 0.1s(100ms)
    clock.tick(27)
    if man.hitbox[1]<goblin.hitbox[1]+goblin.hitbox[3]and man.hitbox[3]+man.hitbox[1]>goblin.hitbox[1]:
                if man.hitbox[0]+man.hitbox[2]>goblin.hitbox[0]and man.hitbox[0]<goblin.hitbox[0]+goblin.hitbox[2]:
                       man.hit(goblin)
                       score-=2
            
    #events:anything that happens from the user(Mouse,Keybors...)
    #checking for events ==>
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    for bullet in bullets:
         if bullet.y-bullet.radius<goblin.hitbox[1]+goblin.hitbox[3]and bullet.y+bullet.radius>goblin.hitbox[1]:
                if bullet.x+bullet.radius>goblin.hitbox[0]and bullet.x-bullet.radius<goblin.hitbox[0]+goblin.hitbox[2]:
                       goblin.hit()
                       bullets.pop(bullets.index(bullet))
                       score+=1
       
         if bullet.x<500 and bullet.x>0:
              bullet.x+=bullet.vel
         else:
                
                bullets.pop(bullets.index(bullet))
       
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
             
             if man.left:
                  facing=-1
             else:
                  facing=1     
             if len(bullets)<1:
                bullets.append(projectile(round(man.x+man.width//2),round(man.y+man.height//2),6,(0,0,0),facing))
                munition=1
                bulletSound.play()
       
    if keys[pygame.K_RIGHT]and man.x<500-man.vel-man.width:
        man.x+=man.vel
        man.right=True
        man.left=False
        man.standing=False
    elif keys[pygame.K_LEFT] and man.x>man.vel:
        man.x-= man.vel
        man.left=True
        man.right=False
        man.standing=False
    else:
        man.standing=True
        man.walkCount=0
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump=True
            man.right=False
            man.left=False
            man.walkCount=0
    else:
        if man.jumpVel>=-10:
            neg=1
            if man.jumpVel<0:
                neg=-1
            man.y-=(man.jumpVel**2)*neg
            man.jumpVel-=1
        else:
            man.isJump=False
            man.jumpVel=10    
    redrawGameWindow()
pygame.quit()
