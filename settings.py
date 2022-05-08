# 属性设置类
import pygame.display


class Settings:
    """项目内属性值的集合类"""

    def __init__(self):
        """初始化项目基本属性"""
        # 屏幕尺寸
        self.v_Info = pygame.display.Info()
        self.full_screen = self.v_Info.current_w, self.v_Info.current_h
        # 设置标准模式窗体尺寸为电脑屏幕大小的2/3
        self.WIDTH, self.HEIGHT = int(self.v_Info.current_w / 3 * 2), int(self.v_Info.current_h / 3 * 2)
        self.screen_size = self.screen_width, self.screen_height = self.WIDTH, self.HEIGHT
        # 屏幕模式标志
        self.screen_type = {'standard': False, 'resizable': False, 'full': False}
        # 屏幕背景色
        self.bg_color = (198, 198, 198)
        # 窗体标题字符串
        self.str_caption = 'QR code'
        # 图片文件链接
        self.image_file = 'images/QR_code.gif'
        # 移动对象移动值
        self.speed = 1
        self.move_x, self.move_y = 1, 1
        # 屏幕刷新帧率
        self.fps = 300
