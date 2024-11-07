import pygame
import requests
import sys
#键盘输入必须是英文，中文无法识别！！！！！！！！！！
# 初始化Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pygame with Flask")

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:  # 按下 'g' 键获取数据
                try:
                    response = requests.get('http://169.254.232.238:5000/get_data')
                    response.raise_for_status()  # 检查请求是否成功
                    data = response.json()
                    print("Received data:", data)
                except requests.exceptions.RequestException as e:
                    print("Error while getting data:", e)

            # 发送数据
            elif event.key == pygame.K_p:  # 按下 'p' 键发送数据
                new_data = {"message": "Hello from Pygame!"}
                try:
                    response = requests.post('http://169.254.232.238:5000/post_data', json=new_data)
                    response.raise_for_status()  # 检查请求是否成功
                    print("Data sent successfully!")
                except requests.exceptions.RequestException as e:
                    print("Error while sending data:", e)
    # 清屏并绘制背景色
    screen.fill(WHITE)
    font = pygame.font.Font(None, 36)
    text = font.render("Press 'g' to get data, 'p' to post data", True, BLACK)
    screen.blit(text, (50, 50))
    pygame.display.flip()

pygame.quit()
sys.exit()
