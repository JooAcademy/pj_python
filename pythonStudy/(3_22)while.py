import pygame

# 전체 스크린의 가로, 세로 크기 설정
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500

# 초기화
pygame.init()

# 스크린 생성
SCREEN = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

# window의 타이틀 설정
pygame.display.set_caption("pygame test")

# Clock 객체 생성
clock = pygame.time.Clock()
playing = True

i = 0
while playing:
    ''' 코드 '''
    
    if (i < 10):
        print(i)
    else :
        pygame.quit()
    
        
    i = i + 1
    
    # fps 설정, while 구문안에 넣는다.
    clock.tick(1)
    