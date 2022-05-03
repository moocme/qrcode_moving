# 二维码的类
import pygame


class QrCode:
    def __init__(self, qrcode_moving):
        self.qc_screen = qrcode_moving.qm_screen.screen
        self.qc_image = pygame.image.load(qrcode_moving.qm_set.image_file)
        self.qc_image_rect = self.qc_image.get_rect()
        self.qc_image_rect.center = qrcode_moving.qm_screen.screen_rect.center

    def blit_qr_code(self):
        self.qc_screen.blit(self.qc_image, self.qc_image_rect)
