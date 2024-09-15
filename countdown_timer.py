import pygame
import cv2
import numpy
import time

pygame.init()

# Set window size to 3840x2160 (4K resolution)
window = pygame.display.set_mode((3840, 2160))
clock = pygame.time.Clock()

# Set the countdown time to 30 minutes (1800 seconds)
total_time = 1800
counter = total_time  # Countdown from 30 minutes

# Define auto-close delay after the timer finishes (20 minutes = 1200 seconds)
post_timer_close_time = 1200  # 20 minutes in seconds

# Define colors
dark_red = (139, 0, 0)
dark_green = (0, 100, 0)

# Adjust the font size for the larger 4K screen
font = pygame.font.SysFont(None, 600)

# Toggle to control whether the numbers are displayed
show_numbers = True  # Set to True to display the numbers

# Timer settings
start_time = time.time()  # Capture the start time

# Track when the timer finishes
timer_finished_time = None  # Will store the time when the timer finishes

# Function to draw the arc using OpenCV and display it in pygame
def drawArcCv2(surf, color, center, radius, width, end_angle):
    # Adjust the start_angle to 12 o'clock (270 degrees or -90 degrees)
    start_angle = 270
    circle_image = numpy.zeros((radius*2+4, radius*2+4, 4), dtype=numpy.uint8)
    circle_image = cv2.ellipse(circle_image, (radius+2, radius+2),
        (radius-width//2, radius-width//2), 0, start_angle, start_angle + end_angle, (*color, 255), width, lineType=cv2.LINE_AA) 
    circle_surface = pygame.image.frombuffer(circle_image.flatten(), (radius*2+4, radius*2+4), 'RGBA')
    surf.blit(circle_surface, circle_surface.get_rect(center=center), special_flags=pygame.BLEND_PREMULTIPLIED)

# Function to draw a dark green circle when the timer reaches 0
def draw_green_circle(surf, color, center, radius):
    pygame.draw.circle(surf, color, center, radius)

# Function to format time for the display
def format_time(counter):
    minutes = counter // 60
    seconds = counter % 60

    # Show only minutes if more than 1 minute remains
    if counter > 60:
        return f"{minutes:02}"  # Display only minutes (MM)
    else:
        return f"{minutes:02}:{seconds:02}"  # Display both minutes and seconds (MM:SS)

# Reset function
def reset_timer():
    global counter, start_time
    counter = total_time
    start_time = time.time()  # Reset the start time

# Main loop
run = True
timer_finished = False  # Track whether the timer has finished

while run:
    clock.tick(120)  # Run at 120 frames per second for smoother transition
    elapsed_time = time.time() - start_time  # Calculate elapsed time since start
    counter = max(0, total_time - int(elapsed_time))  # Update the counter in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and timer_finished:  # Reset the timer when spacebar is pressed
                reset_timer()
                timer_finished_time = None  # Reset the finished time when timer is reset
                timer_finished = False

    # When the timer reaches 0, record the time it finished
    if counter == 0 and not timer_finished:
        timer_finished_time = time.time()  # Capture the time when the timer finishes
        timer_finished = True

    # If the timer has finished, check if 20 minutes (1200 seconds) have passed since it finished
    if timer_finished and timer_finished_time:
        elapsed_after_finish = time.time() - timer_finished_time
        if elapsed_after_finish >= post_timer_close_time:
            run = False  # Exit the loop to close the application after 20 minutes

    # Fill the window background with black
    window.fill((0, 0, 0))

    if counter > 0:
        # Calculate the smooth progress fraction
        fractional_time = (total_time - elapsed_time) / total_time
        arc_angle = 360 * fractional_time

        # Draw the progress arc, increase the radius and width for larger screen
        drawArcCv2(window, dark_red, (1920, 1080), 800, 40, arc_angle)

        # Conditionally display the numbers
        if show_numbers:
            time_str = format_time(counter)
            text = font.render(time_str, True, dark_red)
            text_rect = text.get_rect(center=window.get_rect().center)
            window.blit(text, text_rect)

    else:
        # Draw the dark green circle when the timer reaches 0 with the same size
        draw_green_circle(window, dark_green, (1920, 1080), 800)

    # Update the display
    pygame.display.flip()

pygame.quit()
exit()
