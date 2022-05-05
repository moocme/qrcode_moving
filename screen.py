# 屏幕框架类
import pygame


class Screen:
    """窗体对象的类"""

    def __init__(self, qrcode_moving):
        """初始化屏幕设置"""
        # 设置屏幕模式
        self.screen = pygame.display.set_mode(qrcode_moving.qm_set.screen_size)
        self.screen_rect = self.screen.get_rect()
        
        # 设置窗体标题、图标，引入背景色。
        pygame.display.set_caption(qrcode_moving.qm_set.str_caption)
        self.icon = pygame.image.load(qrcode_moving.qm_set.image_file)
        pygame.display.set_icon(self.icon)
        self.bg_color = qrcode_moving.qm_set.bg_color

    def fill_screen(self):
        """填充窗体背景颜色"""
        self.screen.fill(self.bg_color)
