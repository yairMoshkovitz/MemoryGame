import random
import pygame


q = input("your name is:")
try:
    input_l =int(input("what is your level (max 24):"))
    level = 250 -input_l*10
except:
    print("you over al hhokim try again")
    level = 250 -int(input("what is yoyr level (max 24):"))*10
try:
    n = int(input("num of zogot:"))
except:
    print("your input is invalid, try again")
    n = int(input("num of zogot:"))

rohv = (n*2)**0.5*50//1+100
gova = (n*2)**0.5*50//1



pygame.init()



screen = pygame.display.set_mode((rohv, gova))
white = 255, 255, 255
clock = pygame.time.Clock()

pygame.display.set_caption(q)


class klafim():
    def __init__(self,x,y,color):
       

        self.color = color
        self.x = 50+x
        self.y = 20+y
        pygame.draw.line(screen, white , [self.x ,self.y], [self.x, self.y+30], 40)
        pygame.display.flip()
        self.open = 0
       
    def close(self):
        self.open = 0
        pygame.draw.line(screen, white , [self.x ,self.y], [self.x, self.y+30], 40)
               
           
    def cheak(self,a,b):
        if self.x-20 < a <self.x+30 and self.y <b < self.y+30 :
            self.open = 1
            pygame.draw.line(screen, self.color , [self.x ,self.y], [self.x, self.y+30], 40)
            pygame.display.flip()

j=0
x=0
y=0

k=[0,0,0]
k2=[]

klafim2 = []

l= int(250/level)
for i in range(n):
    for i in range(3):
        k[i] = ((random.randint(0,l))*level)
     #   print(k)
    k2 += [tuple(k)]+[tuple(k)]
   

               
   
 
c = int((n*2)**0.5)
while len(klafim2)< n*2 :
    for i in range(c) :
        if len(klafim2)< n*2 :
            if y< 0:
                y=0
                j=1
            if y > gova-40 :
                x += 50
                y -= gova-50
                j=1

#             if x >   rohv-30:
#                 print("it's too mach")
#                 clock.tick(1/4)

                pygame.quit()

            a = k2[random.randint(0,len(k2))-1]
            klaf = klafim(0+x,0+y,a)
            klafim2 += [klaf]
            k2.remove(a)
            y += 50  #      print(len(klafim2))
    if j != 1:
        x += 50
        y-= 50*c
       
       

while True:
   
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()        

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in  klafim2:
                i.cheak(mouse[0],mouse[1])
               
         #       print(mouse)
          #      print(i.open)
         #   print("-----------------------------")
            p=0
            for i in klafim2:
                if i.open == 1:
                    p += 1
                    k2 += [i]
       #     print(p)
       #     print("-----------------------------")

            if p == 2:
                if k2[-1].color == k2[-2].color:
                  #  k2[-1].open=0
                  #  k2[-2].open=0
                    klafim2.remove(k2[-1])
                    klafim2.remove(k2[-2])
                time.sleep(input_l/4)
                for i in   klafim2:
                    i.close()
                   
        if event.type == pygame.QUIT:
            pygame.quit()
           
           
       
    pygame.display.flip()
