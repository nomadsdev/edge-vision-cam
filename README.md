# EdgeVisionCam

EdgeVisionCam is a real-time edge detection camera application built with Python and Pygame. It captures live video from your webcam, processes the frames with an enhanced edge detection algorithm, and displays the result on your screen.

## Features

- **Real-Time Edge Detection:** Captures live video from your webcam and applies an edge detection algorithm in real-time.
- **Customizable Parameters:** Easily adjust the Gaussian blur sigma, low and high threshold values for edge detection.
- **Simple and Intuitive UI:** Display the processed video feed with a straightforward Pygame-based interface.

## Requirements

- Python 3.x
- Pygame
- NumPy
- SciPy

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/nomadsdev/edge-vision-cam.git
    cd EdgeVisionCam
    ```

2. Install the required Python packages:

    ```bash
    pip install pygame numpy scipy
    ```

3. Run the application:

    ```bash
    python main.py
    ```

## Project Structure

- `main.py`: The main entry point of the application, handling the camera feed and displaying the processed images.
- `camera_handler.py`: Handles the webcam input using Pygame's camera module.
- `display_handler.py`: Manages the display of images on the Pygame window.
- `edge_detection.py`: Contains the edge detection algorithm that processes each frame.

## Usage

1. Start the application by running `main.py`.
2. The camera feed will open, and the edges of objects in the frame will be highlighted.
3. To stop the application, close the window or press `Ctrl+C` in the terminal.

## Customization

You can adjust the parameters for edge detection directly in the `main.py` file:

```python
ed = detect_edges(img, sigma=1.5, low_threshold=50, high_threshold=150)
```
