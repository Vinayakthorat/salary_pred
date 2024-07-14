import pyautogui
import time

while True:

    time.sleep(1)

    # Get the dimensions of the screen
    screen_width, screen_height = pyautogui.size()

    # Calculate the coordinates of the center of the screen
    center_x, center_y = screen_width / 2, screen_height / 2

    # Click on the center of the screen
    # pyautogui.click(center_x, center_y)
    pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
    pyautogui.doubleClick()     # Double click the mouse.
    pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
    time.sleep(1)
    pyautogui.click(center_x+50, center_y+100)

    # Wait for 9 minutes
    print("[Info] Click Done....")
    time.sleep(5)