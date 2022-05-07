# pygame 移动二维码
# 学习练习项目，把学习到的python、pygame知识在一个项目中实践。

# 引入基本支持类
import sys
import pygame

# 引入项目自定义类
from settings import Settings  # 属性设置类
from screen import Screen  # 屏幕框架类
from qr_code import QrCode  # 移动对象（二维码）类


class QrcodeMoving:
    """移动二维码的主类"""

    def __init__(self):
        """初始化主类"""
        # 对Pygame内部各功能模块进行初始化
        pygame.init()
        # 创建一个属性设置类的实例
        self.qm_set = Settings()
        # 创建一个屏幕框架类的实例
        self.qm_screen = Screen(self)
        # 创建一个移动对象（二维码）类的实例
        self.qm_code = QrCode(self)

    def run_game(self):
        """游戏的主循环"""
        while True:
            self._examine_events()
            self.qm_code.qr_code_update()
            self._renovate_screen()

    def _examine_events(self):
        """响应键盘鼠标事件——辅助方法"""
        for event in pygame.event.get():
            # 响应鼠标按窗体X退出
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 响应按下键盘按键事件
                if event.key == pygame.K_q:
                    # 响应键盘按q退出，遗留问题——有什么办法把两个退出响应合并！
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    self.qm_code.flag_left = True
                if event.key == pygame.K_RIGHT:
                    self.qm_code.flag_right = True
                if event.key == pygame.K_UP:
                    self.qm_code.flag_up = True
                if event.key == pygame.K_DOWN:
                    self.qm_code.flag_down = True
                if event.key == pygame.K_F11:
                    # 响应F11全屏显示
                    self.qm_set.screen_type['full'] = True
                if event.key == pygame.K_ESCAPE:
                    # 响应Esc标准显示模式
                    self.qm_set.screen_type['standard'] = True
            elif event.type == pygame.KEYUP:
                # 响应抬起键盘按键事件
                if event.key == pygame.K_LEFT:
                    self.qm_code.flag_left = False
                if event.key == pygame.K_RIGHT:
                    self.qm_code.flag_right = False
                if event.key == pygame.K_UP:
                    self.qm_code.flag_up = False
                if event.key == pygame.K_DOWN:
                    self.qm_code.flag_down = False
            elif event.type == pygame.VIDEORESIZE:
                # 响应鼠标拖拉窗体
                self.qm_set.screen_type['resizable'] = True
                self.qm_set.screen_size = \
                    self.qm_set.screen_width, self.qm_set.screen_height = \
                    event.size[0], event.size[1]

    def _renovate_screen(self):
        """刷新屏幕、移动对象——辅助方法"""
        self.qm_screen.fill_screen()
        self.qm_code.blit_qr_code()
        pygame.display.update()


if __name__ == '__main__':
    # 创建类实例，运行程序。
    qrcode_moving = QrcodeMoving()
    qrcode_moving.run_game()
