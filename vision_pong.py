import pygame
import cv2
import numpy as np
from game_logic import GameState

# Initialize Pygame
pygame.init()

# Create game state
game_state = GameState()

# Set up the display
screen = pygame.display.set_mode((game_state.WIDTH, game_state.HEIGHT))
pygame.display.set_caption("Vision Paddle")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
GREEN = (0, 255, 120)
BLACK = (0, 0, 0)

# Font
font = pygame.font.Font(None, 74)

# Game loop
running = True
clock = pygame.time.Clock()

try:
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update game state
        game_state.update()
        
        # Draw everything
        screen.fill(BLACK)
        
        # Draw paddles
        pygame.draw.rect(screen, BLUE, (50, 
                                      game_state.left_paddle_y - game_state.PADDLE_HEIGHT//2,
                                      game_state.PADDLE_WIDTH, 
                                      game_state.PADDLE_HEIGHT))
        
        pygame.draw.rect(screen, GREEN, (game_state.WIDTH - 50 - game_state.PADDLE_WIDTH,
                                       game_state.right_paddle_y - game_state.PADDLE_HEIGHT//2,
                                       game_state.PADDLE_WIDTH,
                                       game_state.PADDLE_HEIGHT))
        
        # Draw ball
        state = game_state.get_state()
        ball_x, ball_y = state['ball_pos']
        pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), game_state.BALL_SIZE//2)
        
        # Draw center line
        for y in range(0, game_state.HEIGHT, 30):
            pygame.draw.rect(screen, WHITE, (game_state.WIDTH//2 - 1, y, 2, 15))
        
        # Draw scores
        left_score = font.render(str(game_state.left_score), True, BLUE)
        right_score = font.render(str(game_state.right_score), True, GREEN)
        screen.blit(left_score, (game_state.WIDTH//4, 20))
        screen.blit(right_score, (3*game_state.WIDTH//4, 20))
        
        # Update display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(60)

finally:
    # Clean up
    pygame.quit()
    game_state.cleanup()