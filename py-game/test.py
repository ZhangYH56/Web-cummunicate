import pygame
import sys
# 初始化pygame
pygame.init()
# 定义变量
size = width, height = 1000, 600
bg = (255, 255, 255)
# 加载logo图
img = pygame.image.load("D:\\Pictures\\0.jpg")
# 获取图像的位置
position = img.get_rect()
# 创建一个主窗口
screen = pygame.display.set_mode(size)
# 标题
pygame.display.set_caption("C语言中文网")
# 创建游戏主循环
while True:
    # 设置初始值
    site = [0, 0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 图像移动 KEYDOWN 键盘按下事件
        # 通过 key 属性对应按键
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                site[1] -= 8
                print("ysssssss")
            if event.key == pygame.K_DOWN:
                site[1] += 8
            if event.key == pygame.K_LEFT:
                site[0] -= 8
            if event.key == pygame.K_RIGHT:
                site[0] += 8
    # 移动图像
    position = position.move(site)
    # 填充背景
    screen.fill(bg)
    # 放置图片
    screen.blit(img, position)
    # 更新显示界面
    pygame.display.flip()
