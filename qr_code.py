# 二维码的类
import pygame


class QrCode:
    def __init__(self, qrcode_moving):
        self.qc_screen = qrcode_moving.qm_screen.screen
        self.qc_image = pygame.image.load(qrcode_moving.qm_set.image_file)
        self.qc_image_rect = self.qc_image.get_rect()
        self.qc_image_rect.center = qrcode_moving.qm_screen.screen_rect.center
        self.flag_left = False
        self.flag_right = False
        self.flag_up = False
        self.flag_down = False
        self.qc_speed = qrcode_moving.qm_set.speed

    def qr_code_update(self):
        if self.flag_left:
            self.qc_image_rect.centerx -= self.qc_speed
        elif self.flag_right:
            self.qc_image_rect.centerx += self.qc_speed
        elif self.flag_up:
            self.qc_image_rect.centery -= self.qc_speed
        elif self.flag_down:
            self.qc_image_rect.centery += self.qc_speed

    def blit_qr_code(self):
        self.qc_screen.blit(self.qc_image, self.qc_image_rect)
