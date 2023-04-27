import pygame
import random

# 초기화
pygame.init()

# 게임 화면 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball")

# 공 이미지 불러오기
ball_img = pygame.image.load("ball.png")
ball_size = ball_img.get_rect().size
ball_width = ball_size[0]
ball_height = ball_size[1]

# 공 초기 위치
ball_x = screen_width / 2 - ball_width / 2
ball_y = screen_height / 2 - ball_height / 2

# 공 이동 방향
ball_direction_x = random.choice([-1, 1])
ball_direction_y = -1

# 공 이동 속도
ball_speed = 0.1

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키보드 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT]:
        ball_x += ball_speed

    # 공 이동 처리
    ball_x += ball_direction_x * ball_speed
    ball_y += ball_direction_y * ball_speed

    # 공 벽 충돌 처리
    if ball_x < 0 or ball_x >= screen_width - ball_width:
        ball_direction_x *= -2
    if ball_y <= 0:
        ball_direction_y *= -2
    if ball_y >= screen_height - ball_height:
        running = False

    # 화면에 그리기
    screen.fill((255, 255, 255))
    screen.blit(ball_img, (ball_x, ball_y))
    pygame.display.update()

# 게임 종료
pygame.quit()
