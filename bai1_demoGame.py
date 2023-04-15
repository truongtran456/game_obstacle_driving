from email import message
import pygame 
import time
import random

pygame.init()

display_width = 800
display_height =600#tạo kích thước khung

black =(0,0,0)
white=(255,255,255)
red=(255,0,0)

block_color=(53,115,255)#màu vật cản

car_width= 77#chieu rong cua xe 

gameDisplay= pygame.display.set_mode((display_width,display_height))# chieu rong va ngang
pygame.display.set_caption('A bit Racey')#ten game
clock = pygame.time.Clock() #đồng hồ để tính toán trong game

carImg= pygame.image.load('./dist/img/racecar.png')

def things_dodgred(count):#Hàm hiển thị số vật cản
    font = pygame.font.SysFont(None, 25)#font chữ
    text = font.render("Dodgred: "+str(count), True, black)#hiển thị text
    gameDisplay.blit(text,(0,0))# chieu len man hinh ở vị trí 0,0

def things(thingx,thingy, thingw, thingh, color):#5#vẽ ra các vật cản
    pygame.draw.rect(gameDisplay,color ,[thingx,thingy,thingw,thingh])
    

def car(x,y):#2 xuất hiện xe tại vị trí x,y
    gameDisplay.blit(carImg,(x,y))#blit vẽ lên những thứ ta yêu cầu

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):#dinh dang font chu cho thong bao crash'#4
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height)/2)#can giua
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()#màn hình nó cập nhật lại
    
    time.sleep(2)# sau 2s no tự tắt thông báo
    game_loop()#trở về bàn đầu

def crash():#xuat thong bao'#3
    message_display('You Crashed')


def game_loop():#1
    
    x=(display_width * 0.45)# tạo x,y là điểm bắt đầu
    y=(display_height * 0.8)

    x_change=0 #bien khoi tao vi tri cua x
    
    thing_startx= random.randrange(0,display_width)#random ra vi tri x bat ki
    thing_starty= -600 
    thing_speed =7#tốc độ
    thing_width=100
    thing_height =100
    
    dodged=0

    gameExit= False # cho rằng sự cố là sai thi thoat
    while not gameExit: #chạy cho đến khi gặp sự cố thì thôi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#outgame
                pygame.QUIT
                quit() 
                
            if event.type == pygame.KEYDOWN:#phim xuong
                if event.key== pygame.K_LEFT:#mui ten ben trai
                    x_change = -5
                elif event.key ==pygame.K_RIGHT:#mui ten ben phai
                    x_change = 5    #1 lan vay qua phai 5           
            if event.type==pygame.KEYUP:#phim len
                if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                    x_change=0 # giữ nguyên vị trí
        
        x+=x_change      
        gameDisplay.fill(white) # màu nền
        
        #thingx,thingy, thingw, thingh, color
        things(thing_startx,thing_starty, thing_width, thing_height, block_color)#goi things đưa giái trị vào cho vật cản
        thing_starty += thing_speed

        car(x,y)  # gọi hàm car 
        things_dodgred(dodged)
        
         #nếu mà chạy qua 2 mép là out game/gọi hàm crash
        if x > display_width - car_width or x <0:
            crash()
        
        if thing_starty>display_height :# cứ ra khỏi height màn hình là vật cản chạy lại
            thing_starty = 0 - thing_height #vị trí chạy
            thing_startx= random.randrange(0,display_width)#vật cản sẽ xuất hiện random trên màn hình
            dodged += 1 # vật cản cứ xuất hiện lại thì đếm+1
            thing_speed +=1 # sau 1 cái thì vật cản nó nhanh hơn
            #thing_width += (dodged *1.2) # sau 1 cái thì vật cản rộng hơn 1.2 lần
        
        if y < thing_starty + thing_height:
            print('y crossover')
            
            if x> thing_startx and x < thing_startx + thing_width or x+car_width> thing_startx and x+car_width < thing_startx + thing_width:
                print('x crossover')
                crash()
        
        pygame.display.update()#màn hình nó cập nhật lại
        clock.tick(60)#60fps
game_loop()
pygame.quit()#kết thúc
quit()#thoát khỏi ứng dụng và pygame