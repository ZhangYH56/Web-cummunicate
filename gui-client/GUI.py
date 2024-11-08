import pygame
import requests
import sys
from datetime import datetime

# 初始化Pygame
pygame.init()

# 窗口设置
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Real-time Data Display")

# 服务器配置
SERVER_URL = 'http://localhost:5000'  # 可根据实际情况修改

# 颜色配置
COLORS = {
    'background_top': (41, 50, 65),
    'background_bottom': (20, 24, 31),
    'text': (255, 255, 255),
    'table_header': (61, 90, 254),
    'table_row_1': (45, 55, 72),
    'table_row_2': (52, 63, 83),
    'table_border': (80, 90, 120)
}

# 字体设置
font = pygame.font.Font(None, 32)

def draw_gradient_background(surface):
    """绘制渐变背景"""
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        color = [
            COLORS['background_top'][i] + (COLORS['background_bottom'][i] - COLORS['background_top'][i]) * ratio
            for i in range(3)
        ]
        pygame.draw.line(surface, color, (0, y), (WIDTH, y))

def draw_table(surface, data_list):
    """绘制数据表格"""
    # 表格设置
    table_width = 900
    row_height = 50
    col_width = table_width // 5
    start_x = (WIDTH - table_width) // 2
    start_y = 100

    # 表头
    headers = ['Time', 'Name', 'Gender', 'Occupation', 'Hobby']

    # 绘制主表格边框
    table_height = row_height * 6  # 6行（1个表头 + 5个数据行）
    main_table_rect = pygame.Rect(start_x, start_y, table_width, table_height)
    pygame.draw.rect(surface, COLORS['table_border'], main_table_rect, 2, border_radius=5)

    # 绘制表头
    for i, header in enumerate(headers):
        cell_rect = pygame.Rect(start_x + i * col_width, start_y, col_width, row_height)
        pygame.draw.rect(surface, COLORS['table_header'], cell_rect)
        pygame.draw.line(surface, COLORS['table_border'], 
                        (cell_rect.right, start_y), 
                        (cell_rect.right, start_y + table_height), 1)

        header_text = font.render(header, True, COLORS['text'])
        text_rect = header_text.get_rect(center=cell_rect.center)
        surface.blit(header_text, text_rect)

    # 绘制横线
    for row in range(6):
        y = start_y + row * row_height
        pygame.draw.line(surface, COLORS['table_border'], 
                        (start_x, y), 
                        (start_x + table_width, y), 1)

    # 绘制数据行
    display_data = data_list[-5:] if len(data_list) > 0 else []
    for row_idx, data in enumerate(display_data):
        y = start_y + (row_idx + 1) * row_height
        row_color = COLORS['table_row_1'] if row_idx % 2 == 0 else COLORS['table_row_2']

        # 绘制行背景
        row_rect = pygame.Rect(start_x, y, table_width, row_height)
        pygame.draw.rect(surface, row_color, row_rect)

        # 绘制数据
        try:
            values = [
                data.get('time', datetime.now().strftime("%H:%M:%S")),
                data['data'].get('name', 'N/A'),
                data['data'].get('gender', 'N/A'),
                data['data'].get('occupation', 'N/A'),
                data['data'].get('hobby', 'N/A')
            ]

            for col_idx, value in enumerate(values):
                cell_rect = pygame.Rect(start_x + col_width * col_idx, y, col_width, row_height)
                value_text = font.render(str(value), True, COLORS['text'])
                text_rect = value_text.get_rect(center=cell_rect.center)
                surface.blit(value_text, text_rect)
        except (KeyError, TypeError) as e:
            print(f"Invalid data format received: {e}")

def get_data_from_server():
    """从服务器获取数据"""
    try:
        response = requests.get(f'{SERVER_URL}/get_data')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while getting data: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing response: {e}")
        return None

def main():
    """主程序循环"""
    running = True
    data_history = []
    clock = pygame.time.Clock()
    last_update_time = 0
    update_interval = 1000  # 每秒更新一次

    while running:
        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 自动更新数据
        current_time = pygame.time.get_ticks()
        if current_time - last_update_time > update_interval:
            new_data = get_data_from_server()
            if new_data:
                # 只在数据不同时添加新数据
                if not data_history or new_data != data_history[-1]:
                    data_history.append(new_data)
                    # 只保留最新的5条记录
                    if len(data_history) > 5:
                        data_history = data_history[-5:]
            last_update_time = current_time

        # 绘制界面
        draw_gradient_background(screen)
        draw_table(screen, data_history)

        # 绘制标题
        title = font.render("Real-time Data Display", True, COLORS['text'])
        title_rect = title.get_rect(center=(WIDTH // 2, 50))
        screen.blit(title, title_rect)

        # 更新显示
        pygame.display.flip()
        clock.tick(60)

    # 退出程序
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()