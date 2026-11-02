import pygame
from constants import *
from logger import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    ship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    dt: float = 0.0

    while True:
        log_state()
        for event in pygame.event.get():  # get events from the queue
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for steen in asteroids:
            if steen.collides_with(ship):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for curr_shot in shots:
                if steen.collides_with(curr_shot):
                    log_event("asteroid_shot")
                    steen.split()
                    curr_shot.kill()
        for objects in drawable:
            objects.draw(screen)
        pygame.display.flip()  # Update the full display Surface to the screen
        dt = clock.tick(60) / 1000
         
if __name__ == "__main__":
    main()