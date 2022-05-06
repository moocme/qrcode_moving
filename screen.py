# 屏幕框架类
import pygame


class Screen:
    """窗体对象的类"""

    def __init__(self, qrcode_moving):
        """初始化屏幕设置"""
        # 引入主模块中实例化的setting对象
        self.s_setting = qrcode_moving.qm_set
        # 设置屏幕模式
        self.screen = pygame.display.set_mode(self.s_setting.screen_size)
        self.screen_rect = self.screen.get_rect()
        # 设置窗体尺寸、标题、图标、引入背景色、刷新幀率...
        pygame.display.set_caption(self.s_setting.str_caption)
        self.icon = pygame.image.load(self.s_setting.image_file)
        pygame.display.set_icon(self.icon)
        self.bg_color = self.s_setting.bg_color
        # 刷新幀率
        self.fps = self.s_setting.fps
        self.f_clock = pygame.time.Clock()
        # 屏幕尺寸相关值
        self.screen_type = self.s_setting.screen_type
        self.f_screen = self.s_setting.full_screen

    def fill_screen(self):
        """填充窗体背景颜色,限制屏幕刷新幀率"""
        if self.screen_type['full']:
            # 更改setting中的屏幕尺寸（全屏尺寸）
            self.s_setting.screen_width, self.s_setting.screen_height = self.f_screen
            # 设置全屏模式
            self.screen = pygame.display.set_mode(self.f_screen, pygame.FULLSCREEN)
            self.screen_rect = self.screen.get_rect()
            self.screen_type['full'] = False

        self.screen.fill(self.bg_color)
        self.f_clock.tick(self.fps)
