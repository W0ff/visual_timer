
# Countdown Timer with Progress Ring and Auto-Close

This is a countdown timer application built using Python and `pygame`. The timer displays a progress ring that gradually shrinks as time progresses. It also has options to display the remaining time in minutes or minutes and seconds. Once the countdown finishes, the application waits for an additional 20 minutes before automatically closing.

## Features

- **Countdown Timer**: Set for a total of 30 minutes, displayed on a 4K resolution screen (3840x2160).
- **Progress Ring**: A progress ring represents the time remaining, which shrinks from 360 degrees to 0 as the timer runs.
- **Display Modes**: Shows only minutes (`MM`) until the final minute, where it switches to `MM:SS`.
- **Green Circle on Completion**: When the timer reaches 0, the progress ring is replaced with a green circle.
- **Auto-Close**: The application closes automatically 20 minutes after the timer finishes.
- **Smooth Animations**: The timer updates smoothly at 120 frames per second (FPS) for a seamless visual experience.

## Requirements

To run this application, you need the following:
- Python 3.x
- Pygame (`pygame` library)
- OpenCV (`opencv-python` library)
  
You can install the required libraries using `pip`:

```bash
pip install pygame opencv-python numpy
```

## How to Run

1. Clone or download the repository.
2. Run the Python script:

```bash
python countdown_timer.py
```

### Optional Configuration

- **Show/Hide Timer Numbers**: By default, the numbers are shown. To hide the countdown numbers, set `show_numbers = False` in the script.
- **Reset Timer**: Press the spacebar to reset the timer at any time.

## How It Works

1. The timer starts at 30 minutes and displays a progress ring.
2. The remaining time is shown in minutes (`MM`) until the last minute, where it changes to `MM:SS`.
3. When the timer reaches 0, the progress ring is replaced with a dark green circle.
4. After the countdown completes, the application waits for an additional 20 minutes before automatically closing itself.
5. You can reset the timer at any point by pressing the spacebar.

## Customization

- **Change Timer Duration**: The total countdown time is currently set to 30 minutes (1800 seconds). You can modify this by updating the `total_time` variable.
- **Auto-Close Time**: The application waits for 20 minutes (1200 seconds) before closing after the timer finishes. You can change this by modifying the `post_timer_close_time` variable.
- **Screen Resolution**: The application is configured for a 4K screen (`3840x2160`). You can adjust this by changing the window dimensions in the script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
