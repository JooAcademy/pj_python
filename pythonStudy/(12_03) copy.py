### 챗GPT로 보이는 화면 보호기

import pygame
import sys
import time

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 400, 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("시계")

# 폰트 설정
font = pygame.font.Font(None, 36)

def draw_clock():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    text = font.render(current_time, True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))

    # 화면에 시계 그리기
    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.flip()

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_clock()

    # 초당 1번 업데이트
    clock.tick(1)
    
    
    