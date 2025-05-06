# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
import player
from player import Player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    player1 = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        updatable.update(dt)

        for draw in drawable: draw.draw(screen)

        pygame.display.flip()

        #clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
