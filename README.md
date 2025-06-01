# Vision Paddle

A modern take on the classic Pong game, controlled using computer vision! Control the paddles by holding up colored objects in front of your webcam.

## Requirements

- Python 3.7+
- Webcam
- Blue and green objects for paddle control (e.g., colored paper, toys)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/knownstranger-Tapasya/VisionPaddle.git
cd VisionPaddle
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## How to Play

1. Run the game:
```bash
python vision_pong.py
```

2. Control the paddles:
   - **Left Paddle (Blue)**: Hold a blue object in front of your webcam
   - **Right Paddle (Green)**: Hold a green object in front of your webcam

3. Game Rules:
   - Move your paddle to hit the ball
   - Score points when the ball passes your opponent's paddle
   - The ball speeds up slightly each time it hits a paddle
   - Game always runs for full 60 seconds
   - After 60 seconds:
     - Player with higher score wins
     - If tied, game enters Sudden Death mode
     - In Sudden Death, first player to get ahead by 2 points wins!
   - Press ESC to exit when the game ends

## Features

- Real-time computer vision paddle control
- Smooth paddle movement with motion tracking
- Dynamic ball physics with increasing speed
- Score tracking with timer and sudden death mode
- Visual effects and smooth gameplay

## Project Structure

```