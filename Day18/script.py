from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import time

# Initialize the mouse controller
mouse = Controller()

# Flag to control the loop
running = True

# Function to stop the loop when '-' is pressed
def on_press(key):
    global running
    try:
        if key == KeyCode.from_vk(109):  # Virtual key code for numeric '-'
            running = False
            return False  # Stop the listener
    except Exception as e:
        print(f"Error: {e}")

# Main function for clicking
try:
d    with Listener(on_press=on_press) as listener:
        while running:
            mouse.click(Button.left, 1)  # Simulate a left mouse click
            time.sleep(0.1)  # Add delay between clicks to prevent overwhelming the system

        listener.join()  # Wait for the listener to finish

    print("Clicking stopped.")

except KeyboardInterrupt:
    print("Program interrupted.")
