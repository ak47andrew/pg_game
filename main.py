import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_RIGHT,
    K_LEFT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
from pygame.time import Clock
from dts import Position, PosBox
import utils

pygame.init()
pygame.font.init()

WIDTH = 640
HEIGHT = 360
SPEED = 300
CIRCLE_SIZE = 20
TARGET_TPS = 60
FPS_PRECISION = 0
FPS_LOG_LENGHT = 50
FONT = pygame.font.SysFont('Comic Sans MS', 32)
clock = Clock()

pos = Position(WIDTH // 2, HEIGHT // 2)
screen_box = PosBox(
    CIRCLE_SIZE, CIRCLE_SIZE,
    WIDTH - CIRCLE_SIZE, HEIGHT - CIRCLE_SIZE
)
screen = pygame.display.set_mode([WIDTH, HEIGHT])
last_fps = []


def update_keys(keys):
    speed = SPEED / (clock.get_fps() or TARGET_TPS)
    if keys[K_UP]:
        pos.move(0, -speed)
    if keys[K_DOWN]:
        pos.move(0, speed)
    if keys[K_LEFT]:
        pos.move(-speed, 0)
    if keys[K_RIGHT]:
        pos.move(speed, 0)
    pos.limit(screen_box)


def main():
    while True:
        if len(last_fps) > FPS_LOG_LENGHT:
            last_fps.pop(0)
        last_fps.append(round(clock.get_fps() or TARGET_TPS, FPS_PRECISION))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return

        pressed_keys = pygame.key.get_pressed()
        update_keys(pressed_keys)

        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), pos.to_tuple(), CIRCLE_SIZE)
        fps_text_surf = FONT.render(f"min {min(last_fps)} / avg {round(utils.avg(last_fps), FPS_PRECISION)} / max {max(last_fps)}", False, (255, 255, 255))
        screen.blit(fps_text_surf, (0, 0))

        pygame.display.flip()
        clock.tick(TARGET_TPS)


if __name__ == "__main__":
    main()
