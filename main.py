# pygame 移动二维码

import sys
import pygame

from settings import Settings
from screen import Screen
from qr_code import QrCode


class QrcodeMoving:
    def __init__(self):
        pygame.init()
        self.qm_set = Settings()
        self.qm_screen = Screen(self)
        self.qm_code = QrCode(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.qm_screen.fill_screen()
            self.qm_code.blit_qr_code()
            pygame.display.update()


if __name__ == '__main__':
    qrcode_moving = QrcodeMoving()
    qrcode_moving.run_game()
