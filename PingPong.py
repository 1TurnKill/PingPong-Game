import pygame,sys,random

def ball_animation():
    # Movement
    global ball_speed_x,ball_speed_y,player_score,opponent_score,score_time
    ball.x += ball_speed_x # กำหนดให้ความเร็วบอลในการเคลื่อนที่เเกน x + ball_speed_x 
    ball.y += ball_speed_y # กำหนดให้ความเร็วบอลในการเคลื่อนที่เเกน y + ball_speed_y 
    
    if ball.top <= 0 or ball.bottom >= screen_height: # ถ้า ball ในตำเเหน่งด้านบน <= 0 หรือ ball ในตำเเหน่งด้านล่าง >= screen_height
        ball_speed_y *= -1 # ball_speed_y = 7 จาก การตั้งค่าในตอนเเรก => ball_speed_y * -1 => ball_speed_y = -7 => ball.y + ball_speed_y = -7 --> ball เด้งตรงข้ามในเเกน y
  
    if ball.left <= 0: # ถ้า ball ในตำเเหน่งด้านซ้าย <= 0 (ball เลยไปทางด้านซ้าย)
        player_score += 1 # ให้ player_score + 1 
        score_time = pygame.time.get_ticks() # ให้จับ tick ณ ขณะนั้น ปล.tick คือหน่วยเวลาเกม
        
    if ball.right >= screen_width: # ball ในตำเเหน่งด้านขวา >= screen_width (ball เลยไปทางด้านขวา)
        opponent_score += 1 # ให้ opponent_score + 1 
        score_time = pygame.time.get_ticks() # ให้จับ tick ณ ขณะนั้น ปล.tick คือหน่วยเวลาเกม
    
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


def ball_start():
    global ball_speed_y,ball_speed_x,score_time

    ball.center = (screen_width/2,screen_height/2) # ให้ ball อยู่ตรงกลาง
    current_time = pygame.time.get_ticks() # ให้จับ tick ณ ขณะนั้น ปล.tick คือหน่วยเวลาเกม
    
    if current_time - score_time < 700: # ถ้า current_time - score_time น้อยกว่า 700 มิลลิวินาที
        number_three = game_font.render("3",False,dark_red) # ปล.การปรับค่าเป็น False จะทำให้ตัวอักษรไม่ลบรอยหยัก -> ตัวอักษรขรุขระ 
        screen.blit(number_three,(screen_width/2 - 15,screen_height/2 + 20)) # นำ surface(number_three) ของ "3" มาวางบน scrren โดยกำหนดให้อยู่พิกัด x = screen_width/2 - 15 y = screen_height/2 + 20
    if 700 < current_time - score_time < 1400: # ถ้า current_time - score_time มากกว่า 700 มิลลิวินาที เเละ น้อยกว่า 1400 มิลลิวินาที
        number_two = game_font.render("2",False,dark_red) # ปล.การปรับค่าเป็น False จะทำให้ตัวอักษรไม่ลบรอยหยัก -> ตัวอักษรขรุขระ
        screen.blit(number_two,(screen_width/2 - 15,screen_height/2 + 20)) # นำ surface(number_two) ของ "2" มาวางบน scrren โดยกำหนดให้อยู่พิกัด x = screen_width/2 - 15 y = screen_height/2 + 20
    if 1400 < current_time - score_time < 2100: # ถ้า current_time - score_time มากกว่า 1400 มิลลิวินาที เเละ น้อยกว่า 2100 มิลลิวินาที
        number_one = game_font.render("1",False,dark_red) # ปล.การปรับค่าเป็น False จะทำให้ตัวอักษรไม่ลบรอยหยัก -> ตัวอักษรขรุขระ
        screen.blit(number_one,(screen_width/2 - 15,screen_height/2 + 20)) # นำ surface(number_one) ของ "1" มาวางบน scrren โดยกำหนดให้อยู่พิกัด x = screen_width/2 - 15 y = screen_height/2 + 20

    if current_time - score_time < 2100: # ถ้า current_time - score_time น้อยกว่า 2100 มิลลิวินาที 
                                         # ปล.score_time จะเป็นตัวเเปรที่รับค่า tick เพียงครั้งเดียว เพราะ เราเขียนให้ score_time จะมีการรับค่า tick เเค่ตอนที่มีฝั้งใดฝั้งนึงทำเเต้มได้ เท่านั้น
        ball_speed_x,ball_speed_y = 0,0  # ปล.current_time จะเป็นตัวเเปรที่รับค่า tick ครั้งเดียวเหมือนกัน score_time เเต่เนื่องจาก function ของ current_time (ball_start) อยู่ใน While loop ซึ่งถูกเรียกใช้หลายๆครั้ง
                                         # จึงส่งให้ current_time รับค่า tick เพิ่มขึ้นเรื่อยๆ
    else:
        ball_speed_y = 7 * random.choice((1,-1)) # ให้ ball_speed_y มีการ * 1 ไม่ก็ -1 => ส่งผลต่อการเคลื่อนที่ 
        ball_speed_x = 7 * random.choice((1,-1)) # ให้ ball_speed_x มีการ * 1 ไม่ก็ -1 => ส่งผลต่อการเคลื่อนที่
        score_time = None


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
bg_color = pygame.Color('grey12') # ใช้เเบบ Color Object 
light_grey = (200,200,200) # ใช้เเบบ RGB 
dark_red = (139,0,0) # ใช้เเบบ RGB 

# Animation
ball_speed_x = 7 * random.choice((1,-1)) # ball_speed_x เท่ากับ 7 เเละให้มีการคูณ 1 หรือ -1
ball_speed_y = 7 * random.choice((1,-1)) # ball_speed_y เท่ากับ 7 เเละให้มีการคูณ 1 หรือ -1
player_speed = 0 # player_speed เท่ากับ 0
opponent_speed = 7 # player_speed เท่ากับ 0

# Text ตัวเเปร
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("Font/PressStart2P-vaV7.ttf",32) # นำ font เข้า --> เป็น Font PressStart2P ขนาด 32px 

# Score Timer (ตัวเเปรสำหรับเก็บค่าเวลา)
score_time = None # ปล.ยังไม่มีการกำหนดค่าให้กับ score_time

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
                player_speed += 6 # player_speed = 0 จาก การตั้งค่าในตอนเเรก =>player_speed + 6 => player_speed = 6 => player.y + player_speed = 6 --> player เคลื่อนที่ลง 

            if event.key == pygame.K_UP: # ถ้ามีเหตุการณ์ที่กดลูกศรขึ้น
                player_speed -= 6 # player_speed = 0 จาก การตั้งค่าในตอนเเรก => player_speed - 6 => player_speed = -6 => player.y + player_speed = -6 --> player เคลื่อนที่ขึ้น

        if event.type == pygame.KEYUP: # ถ้ามี event การปล่อยปุ่ม 

            if event.key == pygame.K_DOWN: # ถ้ามีเหตุการณ์ที่ปล่อยลูกศรลง
                player_speed -= 6 # player_speed = 6 จาก pygame.K_DOWN(pygame.KEYDOWN) => player_speed - 6 => player_speed = 0 => player.y + player_speed = 0 --> player หยุดนิ่ง
                
            if event.key == pygame.K_UP: # ถ้ามีเหตุการณ์ที่ปล่อยลูกศรขึ้น
                player_speed += 6 # player_speed = -6 จาก pygame.K_UP(pygame.KEYDOWN) => player_speed + 6 => player_speed = 0 => player.y + player_speed = 0 --> player หยุดนิ่ง

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

    if score_time: # หาก score_time มีค่า => หากมีผู้เล่นฝั้งใดฝั้งนึงทำเเต้มได้ scroe_time ก็จะมีนับค่า tick ณ ขณะนั้น ส่งผลให้ scrore_time มีค่า
        ball_start() # จะมีการเรียกใช้ ball_start()
        
                                                                                                # (screen_width/2,screen_height) ให้จุดเริ่มต้น เริ่มที่ x = screen_width/2 เเละ y = screen_height
    player_text = game_font.render(f"{player_score}",False,light_grey) # ปล.การปรับค่าเป็น False จะทำให้ตัวอักษรไม่ลบรอยหยัก -> ตัวอักษรขรุขระ
    screen.blit(player_text,(660,470)) # นำ surface(player_text) ของ player_score มาวางบน scrren โดยกำหนดให้อยู่พิกัด x = 660 y = 470

    opponent_text = game_font.render(f"{opponent_score}",False,light_grey) # ปล.การปรับค่าเป็น False จะทำให้ตัวอักษรไม่ลบรอยหยัก -> ตัวอักษรขรุขระ
    screen.blit(opponent_text,(590,470)) # นำ surface(opponent_text) ของ opponent_score  มาวางบน scrren โดยกำหนดให้อยู่พิกัด x = 590 y = 470


    # ปล.เรื่องลำดับของ code จะทำงานจากบนลงล่างเสมอ ดังนั้น
    # องค์ประกอบเเรก screen.fill(bg_color) จะอยู่ล่างสุดของเฟรม
    # องค์ประกอบอื่นจะอยู่บน screen.fill(bg_color) ตามลำดับ

    pygame.display.flip()
    clock.tick(60) # การกำหนดความเร็วในการทำงานของ loop => fps = 60