import sys
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Set the background color.
    bg_color = (230, 230, 230)

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()


run_game()
