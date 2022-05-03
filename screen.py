# 屏幕框架类
import pygame


class Screen:
    def __init__(self, qrcode_moving):
        self.screen = pygame.display.set_mode(qrcode_moving.qm_set.screen_size)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption(qrcode_moving.qm_set.str_caption)
        self.icon = pygame.image.load(qrcode_moving.qm_set.image_file)
        pygame.display.set_icon(self.icon)
        self.bg_color = qrcode_moving.qm_set.bg_color

    def fill_screen(self):
        self.screen.fill(self.bg_color)
