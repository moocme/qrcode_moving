# 移动对象（二维码）类，选择二维码图片仅仅是学习项目需要一个移动对象。
import pygame


class QrCode:
    """项目内移动对象（二维码）类"""

    def __init__(self, qrcode_moving):
        """初始化移动对象"""
        # 引入窗体对象属性
        self.qc_screen = qrcode_moving.qm_screen.screen
        self.qc_screen_rect = qrcode_moving.qm_screen.screen_rect
        # 引入属性设置对象属性
        self.qc_set = qrcode_moving.qm_set
        # 移动对象二维码的属性设置
        self.qc_image = pygame.image.load(self.qc_set.image_file)
        self.qc_image_rect = self.qc_image.get_rect()
        # 把屏幕中心位置数据赋值给移动对象的位置数据
        self.qc_image_rect.center = qrcode_moving.qm_screen.screen_rect.center
        # 键盘按键产生的移动标志
        self.flag_left = False
        self.flag_right = False
        self.flag_up = False
        self.flag_down = False
        # 鼠标按键标志
        self.sign = self.qc_set.sign
        # 引入移动值
        self.qc_speed = qrcode_moving.qm_set.speed

    def qr_code_update(self):
        """移动对象的属性更新"""
        self._keyboard_control()  # 响应键盘事件
        # 最小化响应鼠标按键时程序暂停
        if pygame.display.get_active() and self.sign:
            self._loops_method()  # 控制移动对象——走马灯效果
            self._bounce_method()  # 控制移动对象——窗体内反弹效果

    def blit_qr_code(self):
        """绘制移动对象"""
        self.qc_screen.blit(self.qc_image, self.qc_image_rect)

    def _keyboard_control(self):
        """响应键盘事件——辅助方法"""
        # 根据移动标志更新移动对象的中心x值、中心y值。
        if self.flag_left:
            self.qc_image_rect.centerx -= self.qc_speed
            # 移动对象自动和操控之间的协调性
            if self.qc_set.move_x > 0:
                self.qc_set.move_x = - self.qc_set.move_x
        if self.flag_right:
            self.qc_image_rect.centerx += self.qc_speed
            if self.qc_set.move_x < 0:
                self.qc_set.move_x = - self.qc_set.move_x
        if self.flag_up:
            self.qc_image_rect.centery -= self.qc_speed
            if self.qc_set.move_y > 0:
                self.qc_set.move_y = - self.qc_set.move_y
        if self.flag_down:
            self.qc_image_rect.centery += self.qc_speed
            if self.qc_set.move_y < 0:
                self.qc_set.move_y = - self.qc_set.move_y

    def _loops_method(self):
        """控制移动对象——走马灯效果——辅助方法"""
        if self.qc_image_rect.left < 0:
            self.qc_image_rect.right = self.qc_set.screen_width - 1
        if self.qc_image_rect.right > self.qc_set.screen_width:
            self.qc_image_rect.left = 1
        if self.qc_image_rect.top < 0:
            self.qc_image_rect.bottom = self.qc_set.screen_height - 1
        if self.qc_image_rect.bottom > self.qc_set.screen_height:
            self.qc_image_rect.top = 1

    def _bounce_method(self):
        """控制移动对象——窗体内反弹效果"""
        self.qc_image_rect.centerx += self.qc_set.move_x
        self.qc_image_rect.centery += self.qc_set.move_y
        if self.qc_image_rect.left <= 0:
            self.qc_set.move_x = - self.qc_set.move_x
        if self.qc_image_rect.right >= self.qc_set.screen_width:
            self.qc_set.move_x = - self.qc_set.move_x
        if self.qc_image_rect.top <= 0:
            self.qc_set.move_y = - self.qc_set.move_y
        if self.qc_image_rect.bottom >= self.qc_set.screen_height:
            self.qc_set.move_y = - self.qc_set.move_y
