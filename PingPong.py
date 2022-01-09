import pygame,sys

pygame.init() # เริ่มต้นโมดูลของ pygame ทั้งหมด เเละ ไว้ใช้สำหรับ run เกมชนิดต่างๆ
clock = pygame.time.Clock() # การกำหนดความเร็วในการทำงานของ loop => ตัวกำหนดค่า fps


screen_width = 1280 # ขนาดความกว้างของหน้าจอ
screen_height = 960 # ขนาดความสูงของหน้าจอ
screen = pygame.display.set_mode((screen_width,screen_height)) # ขนาดหน้าจอ
pygame.display.set_caption('Pong') # เป็นการตั้งชื่อหน้าต่างว่า Pong

# while loop = ให้เกมมีการอัพเดต
# for loop   = ตรวจการกระทำของผู้ใช้ทั้งหมด
while True: 
    for event in pygame.event.get(): 
        # event การออกเกม
        if event.type == pygame.QUIT:
            pygame.quit()               
            sys.exit()


    pygame.display.flip()
    clock.tick(60) # การกำหนดความเร็วในการทำงานของ loop => fps = 60