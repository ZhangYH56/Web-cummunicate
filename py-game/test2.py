import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("键盘输入显示字母")

# 设置字体
font = pygame.font.Font(None, 100)

# 用于保存显示的字母
current_letter = ""

# 游戏主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                current_letter = "G"
            elif event.key == pygame.K_p:
                current_letter = "P"

    # 填充背景色
    screen.fill((255, 255, 255))

    # 渲染字母
    if current_letter:
        text = font.render(current_letter, True, (0, 0, 0))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(60)