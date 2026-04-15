import pygame
import datetime

class MickeyClock:
    def __init__(self, hand_image):
        self.hand = pygame.image.load(hand_image).convert_alpha()

    def get_time_angles(self):
        now = datetime.datetime.now()
        return now.second * 6, now.minute * 6

    def draw(self, screen, center):
        sec_angle, min_angle = self.get_time_angles()

        #  большая секундная
        sec_hand = pygame.transform.scale(self.hand, (320, 20))
        sec_hand = pygame.transform.rotate(sec_hand, -sec_angle)
        screen.blit(sec_hand, sec_hand.get_rect(center=center))

        #  большая минутная
        min_hand = pygame.transform.scale(self.hand, (260, 35))
        min_hand = pygame.transform.rotate(min_hand, -min_angle)
        screen.blit(min_hand, min_hand.get_rect(center=center))