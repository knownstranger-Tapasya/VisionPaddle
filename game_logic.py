import cv2
import numpy as np

class GameState:
    def __init__(self):
        # Window dimensions
        self.WIDTH = 800
        self.HEIGHT = 600
        
        # Paddle dimensions
        self.PADDLE_WIDTH = 15
        self.PADDLE_HEIGHT = 90
        
        # Ball dimensions
        self.BALL_SIZE = 15
        
        # Initialize positions
        self.left_paddle_y = self.HEIGHT // 2
        self.right_paddle_y = self.HEIGHT // 2
        self.ball_x = self.WIDTH // 2
        self.ball_y = self.HEIGHT // 2
        
        # Initialize speeds
        self.PADDLE_SPEED = 7
        self.ball_speed_x = 7
        self.ball_speed_y = 7
        
        # Initialize scores
        self.left_score = 0
        self.right_score = 0
        
        # Initialize camera
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        
        # Color ranges in HSV
        self.lower_blue = np.array([95, 80, 80])
        self.upper_blue = np.array([135, 255, 255])
        self.lower_green = np.array([35, 80, 80])
        self.upper_green = np.array([85, 255, 255])

    def detect_color(self, frame, lower_color, upper_color):
        """Detect the position of a colored object"""
        frame = cv2.resize(frame, (320, 240))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_color, upper_color)
        
        y_coords = np.where(mask > 0)[0]
        if len(y_coords) > 0:
            cy = int(np.mean(y_coords)) * 2
            return cy
        return None

    def update(self):
        """Update game state"""
        # Get camera input
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            
            # Detect colors
            blue_y = self.detect_color(frame, self.lower_blue, self.upper_blue)
            green_y = self.detect_color(frame, self.lower_green, self.upper_green)
            
            # Update paddle positions
            if blue_y is not None:
                target_y = (blue_y / 480) * self.HEIGHT
                self.left_paddle_y += (target_y - self.left_paddle_y) * 0.2
            
            if green_y is not None:
                target_y = (green_y / 480) * self.HEIGHT
                self.right_paddle_y += (target_y - self.right_paddle_y) * 0.2
            
            # Keep paddles in bounds
            self.left_paddle_y = np.clip(self.left_paddle_y, 
                                       self.PADDLE_HEIGHT//2, 
                                       self.HEIGHT - self.PADDLE_HEIGHT//2)
            self.right_paddle_y = np.clip(self.right_paddle_y, 
                                        self.PADDLE_HEIGHT//2, 
                                        self.HEIGHT - self.PADDLE_HEIGHT//2)
            
            # Move ball
            self.ball_x += self.ball_speed_x
            self.ball_y += self.ball_speed_y
            
            # Ball collision with top and bottom
            if self.ball_y <= 0 or self.ball_y >= self.HEIGHT:
                self.ball_speed_y *= -1
            
            # Ball collision with paddles
            left_paddle_rect = {
                'x': 50,
                'y': self.left_paddle_y - self.PADDLE_HEIGHT//2,
                'width': self.PADDLE_WIDTH,
                'height': self.PADDLE_HEIGHT
            }
            
            right_paddle_rect = {
                'x': self.WIDTH - 50 - self.PADDLE_WIDTH,
                'y': self.right_paddle_y - self.PADDLE_HEIGHT//2,
                'width': self.PADDLE_WIDTH,
                'height': self.PADDLE_HEIGHT
            }
            
            # Check paddle collisions
            if (self.ball_x <= left_paddle_rect['x'] + left_paddle_rect['width'] and
                self.ball_x >= left_paddle_rect['x'] and
                self.ball_y >= left_paddle_rect['y'] and
                self.ball_y <= left_paddle_rect['y'] + left_paddle_rect['height']):
                self.ball_speed_x *= -1.1  # Increase speed slightly
                
            if (self.ball_x + self.BALL_SIZE >= right_paddle_rect['x'] and
                self.ball_x <= right_paddle_rect['x'] + right_paddle_rect['width'] and
                self.ball_y >= right_paddle_rect['y'] and
                self.ball_y <= right_paddle_rect['y'] + right_paddle_rect['height']):
                self.ball_speed_x *= -1.1  # Increase speed slightly
            
            # Score points
            if self.ball_x <= 0:
                self.right_score += 1
                self.reset_ball()
            elif self.ball_x >= self.WIDTH:
                self.left_score += 1
                self.reset_ball()
            
            return frame
        return None

    def reset_ball(self):
        """Reset ball to center with random direction"""
        self.ball_x = self.WIDTH // 2
        self.ball_y = self.HEIGHT // 2
        self.ball_speed_x = 7 * (1 if np.random.random() > 0.5 else -1)
        self.ball_speed_y = 7 * (1 if np.random.random() > 0.5 else -1)

    def get_state(self):
        """Return current game state"""
        return {
            'ball_pos': (self.ball_x, self.ball_y),
            'left_paddle_y': self.left_paddle_y,
            'right_paddle_y': self.right_paddle_y,
            'left_score': self.left_score,
            'right_score': self.right_score
        }
    
    def cleanup(self):
        """Release camera resources"""
        self.cap.release()
        cv2.destroyAllWindows() 