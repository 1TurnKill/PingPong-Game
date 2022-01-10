import pygame,sys,random

def ball_animation():
    # Movement
    global ball_speed_x,ball_speed_y  
    ball.x += ball_speed_x # กำหนดให้ความเร็วบอลในการเคลื่อนที่เเกน x + ball_speed_x 
    ball.y += ball_speed_y # กำหนดให้ความเร็วบอลในการเคลื่อนที่เเกน y + ball_speed_y 

    if ball.top <= 0 or ball.bottom >= screen_height: # ถ้า ball ในตำเเหน่งด้านบน <= 0 หรือ ball ในตำเเหน่งด้านล่าง >= screen_height
        ball_speed_y *= -1 # ball_speed_y = 7 จาก การตั้งค่าในตอนเเรก => ball_speed_y * -1 => ball_speed_y = -7 => ball.y + ball_speed_y = -7 --> ball เด้งตรงข้ามในเเกน y
    if ball.left <= 0 or ball.right >= screen_width: # ถ้า ball ในตำเเหน่งด้านซ้าย <= 0 หรือ ball ในตำเเหน่งด้านขวา >= screen_width
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent): # ถ้า ball ชนกับ player หรือ ball ชนกับ opponent
        ball_speed_x *= -1 # ball เด้งตรงข้ามในเเกน x

def player_animation():
    player.y += player_speed # กำหนดให้ความเร็ว player ในเเกน y + player_speed
    # กำหนดขอบการเคลื่อนที่ให้กับ player
    if player.top <= 0: # ถ้า player ในตำเเหน่งด้านบน <= 0
        player.top = 0 # ให้ player ในตำเเหน่งด้านบน อยู่ในตำเเหน่งที่ 0
    if player.bottom >= screen_height: # ถ้า player ในตำเเหน่งด้านล่าง >= screen_height
        player.bottom = screen_height # ให้ player ในตำเเหน่งด้านล่าง อยู่ในตำเเหน่งที่ screen_height

def opponent_ai():
    if opponent.top < ball.y: # ถ้า opponent ตำเเหน่งด้านบน น้อยกว่า ball ในเเกน y (opponent ตำเเหน่งด้านบน อยู่เหนือกว่า ball ตำเเหน่ง center)
        opponent.top += opponent_speed # ให้ opponent ตำเเหน่งด้านบน + opponent_speed => ทำให้ opponent เคลื่อนที่ลง 
    if opponent.bottom > ball.y: # ถ้า opponent ตำเเหน่งด้านล่าง มากกว่า ball ในเเกน y (opponent ตำเเหน่งด้านล่าง อยู่ต่ำกว่า ball ตำเเหน่ง center)
        opponent.bottom -= opponent_speed # ให้ opponent ตำเเหน่งด้านล่าง - opponent_speed => ทำให้ opponent เคลื่อนที่ขึ้น
    if opponent.top <= 0: # ถ้า player ในตำเเหน่งด้านบน <= 0
        opponent.top = 0 # ให้ player ในตำเเหน่งด้านบน อยู่ในตำเเหน่งที่ 0
    if opponent.bottom >= screen_height: # ถ้า player ในตำเเหน่งด้านล่าง >= screen_height
        opponent.bottom = screen_height # ให้ player ในตำเเหน่งด้านล่าง อยู่ในตำเเหน่งที่ screen_height

def ball_restart():
    global ball_speed_y,ball_speed_x
    ball.center = (screen_width/2,screen_height/2) # ให้ ball เริ่มใหม่ตรงกลาง
    ball_speed_y *= random.choice((1,-1)) # ให้ ball_speed_y มีการ * 1 ไม่ก็ -1 => ส่งผลต่อการเคลื่อนที่ 
    ball_speed_x *= random.choice((1,-1)) # ให้ ball_speed_x มีการ * 1 ไม่ก็ -1 => ส่งผลต่อการเคลื่อนที่


pygame.init() # เริ่มต้นโมดูลของ pygame ทั้งหมด เเละ ไว้ใช้สำหรับ run เกมชนิดต่างๆ
clock = pygame.time.Clock() # การกำหนดความเร็วในการทำงานของ loop => ตัวกำหนดค่า fps

screen_width = 1280 # ขนาดความกว้างของหน้าจอ
screen_height = 960 # ขนาดความสูงของหน้าจอ
screen = pygame.display.set_mode((screen_width,screen_height)) # ขนาดหน้าจอ
pygame.display.set_caption('Pong') # เป็นการตั้งชื่อหน้าต่างว่า Pong

# สร้าง Rectangle
# ball
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30) # pygame.Rect(x,y,width,height) = x เเละ y เป็นพิกัดสำหรับการเคลื่อนย้าย Rect ซึ่งจะอยู่มุมซ้ายบน 
                                                                   #                                 width เเละ height เป็นการกำหนดความ กว้างเเละสูงของ Rect
                                                                   # ปล.-15 เพื่อที่จะให้มันอยู่ตรงกลาง
# player                                                                    
player = pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140)
# opponent 
opponent = pygame.Rect(10,screen_height/2 - 70,10,140)

# Color
bg_color = pygame.Color('grey12') # ใช้เเบบ Color Object => สี background
light_grey = (200,200,200) # ใช้เเบบ RGB => สี player เเละ opponent

# Animation
ball_speed_x = 7 * random.choice((1,-1)) # ball_speed_x เท่ากับ 7 เเละให้มีการคูณ 1 หรือ -1
ball_speed_y = 7 * random.choice((1,-1)) # ball_speed_y เท่ากับ 7 เเละให้มีการคูณ 1 หรือ -1
player_speed = 0 # player_speed เท่ากับ 0
opponent_speed = 7 # player_speed เท่ากับ 0

# while loop = ให้เกมมีการอัพเดต
# for loop   = ตรวจการกระทำของผู้ใช้ทั้งหมด
while True: 
    for event in pygame.event.get(): 
        # event การออกเกม
        if event.type == pygame.QUIT:
            pygame.quit()               
            sys.exit()
        # event การควบคุมเคลื่อนไหว player จาก keyboard
        if event.type == pygame.KEYDOWN: # ถ้ามี event การกดปุ่ม 

            if event.key == pygame.K_DOWN: # ถ้ามีเหตุการณ์ที่กดลูกศรลง
                player_speed += 7 # player_speed = 0 จาก การตั้งค่าในตอนเเรก =>player_speed + 7 => player_speed = 7 => player.y + player_speed = 7 --> player เคลื่อนที่ลง 

            if event.key == pygame.K_UP: # ถ้ามีเหตุการณ์ที่กดลูกศรขึ้น
                player_speed -= 7 # player_speed = 0 จาก การตั้งค่าในตอนเเรก => player_speed - 7 => player_speed = -7 => player.y + player_speed = -7 --> player เคลื่อนที่ขึ้น

        if event.type == pygame.KEYUP: # ถ้ามี event การปล่อยปุ่ม 

            if event.key == pygame.K_DOWN: # ถ้ามีเหตุการณ์ที่ปล่อยลูกศรลง
                player_speed -= 7 # player_speed = 7 จาก pygame.K_DOWN(pygame.KEYDOWN) => player_speed - 7 => player_speed = 0 => player.y + player_speed = 0 --> player หยุดนิ่ง
                
            if event.key == pygame.K_UP: # ถ้ามีเหตุการณ์ที่ปล่อยลูกศรขึ้น
                player_speed += 7 # player_speed = -7 จาก pygame.K_UP(pygame.KEYDOWN) => player_speed + 7 => player_speed = 0 => player.y + player_speed = 0 --> player หยุดนิ่ง

    # ตรรกะการทำงานของเกม
    ball_animation()
    player_animation()
    opponent_ai()

    # วาด Rectangle
    screen.fill(bg_color) #.fill การกำหนดสีให้กับ screen
    pygame.draw.rect(screen,light_grey,player)   # pygame.draw.rect(screen,color,rect)    "ทรงสี่เหลี่ยม"        => screen เป็นพื้นที่สำหรับวาง rect
                                                 # pygame.draw.ellipse(screen,color,rect) "ทรงกลม"              color เป็นสีสำหรับ rect
                                                 #                                                               rect  
    pygame.draw.rect(screen,light_grey,opponent) 
    pygame.draw.ellipse(screen,light_grey,ball) # ปล.เนื่องจาก ball มีการตั้งค่าให้ width เเละ height เทากันเลยทำรูปทรงออกเป็นวงกลม
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height)) # pygame.draw.aaline(screen,color,start point,end point) "เป็นเส้นเเบ่งระหว่าง 2 ฝั้ง"
                                                                                            # (screen_width/2,0) ให้จุดเริ่มต้น เริ่มที่ x = screen_width/2 เเละ y = 0
                                                                                            # (screen_width/2,screen_height) ให้จุดเริ่มต้น เริ่มที่ x = screen_width/2 เเละ y = screen_height
    # ปล.เรื่องลำดับของ code จะทำงานจากบนลงล่างเสมอ ดังนั้น
    # องค์ประกอบเเรก screen.fill(bg_color) จะอยู่ล่างสุดของเฟรม
    # องค์ประกอบอื่นจะอยู่บน screen.fill(bg_color) ตามลำดับ

    pygame.display.flip()
    clock.tick(60) # การกำหนดความเร็วในการทำงานของ loop => fps = 60