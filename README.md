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
   - First player to score 5 points wins!

## Features

- Real-time computer vision paddle control
- Smooth paddle movement with motion tracking
- Dynamic ball physics with increasing speed
- Score tracking
- Visual effects and smooth gameplay

## Project Structure

```
VisionPaddle/
├── vision_pong.py     # Main game file with Pygame display and game loop
├── game_logic.py      # Core game logic, physics, and computer vision
├── requirements.txt   # Python dependencies
└── README.md         # Project documentation
```

## Tips for Best Performance

1. Lighting:
   - Ensure good, consistent room lighting
   - Avoid strong backlighting
   - Minimize shadows in play area

2. Color Objects:
   - Use solid colored objects (not patterned)
   - Blue should be distinctly blue (not purple or turquoise)
   - Green should be distinctly green (not yellow-green)
   - Avoid reflective materials

3. Camera Setup:
   - Position yourself with enough distance from the camera
   - Keep the background clean and free of similar colors
   - Make sure no other applications are using the camera

## Troubleshooting

If the paddle movement is not responsive:
- Ensure you have good lighting
- Use objects with clear, solid colors (blue for left, green for right)
- Make sure your webcam is working and properly connected
- Close other applications that might be using the camera

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- OpenCV for computer vision capabilities
- Pygame for game rendering
- The Python community for various helpful resources

## Version History
- v1.0.0 (2024-03-XX)
  - Initial release
  - Basic game functionality
  - Color-based paddle control
  - Score tracking 