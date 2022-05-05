# 属性设置类

class Settings:
    """项目内属性值的集合类"""

    def __init__(self):
        """初始化项目基本属性"""
        # 屏幕尺寸
        self.screen_size = self.screen_width, self.screen_height = (1200, 800)

        # 屏幕背景色
        self.bg_color = (198, 198, 198)

        # 窗体标题字符串
        self.str_caption = 'QR code'

        # 图片文件链接
        self.image_file = 'images/QR_code.gif'

        # 对象移动值
        self.speed = 1
