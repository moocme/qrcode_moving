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
            self._examine_events()
            self.qm_code.qr_code_update()
            self._renovate_screen()

    def _examine_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.qm_code.flag_left = True
                if event.key == pygame.K_RIGHT:
                    self.qm_code.flag_right = True
                if event.key == pygame.K_UP:
                    self.qm_code.flag_up = True
                if event.key == pygame.K_DOWN:
                    self.qm_code.flag_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.qm_code.flag_left = False
                if event.key == pygame.K_RIGHT:
                    self.qm_code.flag_right = False
                if event.key == pygame.K_UP:
                    self.qm_code.flag_up = False
                if event.key == pygame.K_DOWN:
                    self.qm_code.flag_down = False

    def _renovate_screen(self):
        self.qm_screen.fill_screen()
        self.qm_code.blit_qr_code()
        pygame.display.update()


if __name__ == '__main__':
    qrcode_moving = QrcodeMoving()
    qrcode_moving.run_game()
