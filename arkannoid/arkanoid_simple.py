import pygame
import sys

# 게임 화면 설정
pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Arkanoid")

clock = pygame.time.Clock()


# 게임 요소 설정
paddle = pygame.Rect((screen_width - 100) / 2, screen_height - 20, 100, 10)
ball = pygame.Rect(screen_width / 2 - 7, screen_height - 40, 15, 15)
bricks = []
for i in range(10):
    brick = pygame.Rect(60 * i + 20, 50, 50, 20)
    bricks.append(brick)

ball_speed_x = 5
ball_speed_y = -5
paddle_speed = 1

# 게임 루프
while True:
    clock.tick(60) # 초당 60 프레임으로 설정
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_speed = -10
            elif event.key == pygame.K_RIGHT:
                paddle_speed = 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle_speed = 0

# 공 이동
    ball.x += ball_speed_x
    ball.y += ball_speed_y



# 벽 충돌 처리
    if ball.left < 0 or ball.right > screen_width:
        ball_speed_x *= -1
    if ball.top < 0:
        ball_speed_y *= -1
    if ball.bottom > screen_height:
        pygame.quit()
        sys.exit()

# 패들 이동
    paddle.x += paddle_speed
    if paddle.left < 0:
        paddle.left = 0
    elif paddle.right > screen_width:
        paddle.right = screen_width
        
# 패들 충돌 처리
    if ball.colliderect(paddle):
        ball_speed_y *= -1

# 벽돌 충돌 처리
    for brick in bricks:
        if ball.colliderect(brick):
            ball_speed_y *= -1
            bricks.remove(brick)
            break




# 게임 화면 업데이트
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.draw.circle(screen, (255, 255, 255), (ball.x + 7, ball.y + 7), 7)
    #pygame.draw.circle(screen, (255, 255, 255), (int(ball.x), int(ball.y)), 7)
    for brick in bricks:
        pygame.draw.rect(screen, (255, 255, 255), brick)
    pygame.display.update()
