import pyautogui
import configparser
import time
import os
import keyboard
import sys

file_path = os.path.dirname(sys.argv[0])
file_path_img = os.path.join(file_path, "img")

config_dir = os.path.join(file_path, "cfg", "config.ini")


# Path to the INI file
ini_file = config_dir

def load_ini(filename):
    config = configparser.ConfigParser()
    if os.path.exists(filename):
        config.read(filename)
    return config

def save_ini(config, filename):
    with open(filename, "w") as configfile:
        config.write(configfile)

def get_region(name, description):
    pyautogui.alert(f"{description}\n\n1. Move the mouse to the top-left corner and press 'X'.\n2. Move the mouse to the bottom-right corner and press 'X' again.\n\nMake sure the selected area is slightly larger than the target but not too large.")

    start_x, start_y = None, None
    end_x, end_y = None, None

    while start_x is None or end_x is None:
        if keyboard.is_pressed('x'):
            x, y = pyautogui.position()
            if start_x is None:
                start_x, start_y = x, y
            else:
                end_x, end_y = x, y
                break  # Both points have been set
            while keyboard.is_pressed('x'):
                time.sleep(0.1)  # Wait until key is released

    width = end_x - start_x
    height = end_y - start_y

    return f"{start_x},{start_y},{width},{height}"

def get_position(name, description):
    pyautogui.alert(f"{description}\n\nMove your mouse to the desired position and press 'X'.")

    while True:
        if keyboard.is_pressed('x'):
            x, y = pyautogui.position()
            while keyboard.is_pressed('x'):
                time.sleep(0.1)  # Wait until key is released
            return f"{x},{y}"

def get_screen_resolution():
    width, height = pyautogui.size()
    return f"0,0,{width},{height}"

def main():
    config = load_ini(ini_file)

    regions = [
        ("ocv", "button_region", "Mark the area where the fertilizer purchase button is located. Make it slightly larger than the button but not too large."),
        ("ocv", "shop_open_region", "Mark the area where the text 'SHOP' appears when you open the vendor menu. This is at the top of the shop window."),
        ("ocv", "inv_open_region", "Mark the area where the text 'INVENTORY' appears."),
        ("ocv", "esc_region", "Press ESC so the main menu appears, then mark the area where the RUST logo is displayed.")
    ]

    positions = [
        ("Klick", "buy_button_pos", "Move your mouse to the exact position of the buy button and press 'X'."),
        ("Klick", "buy_button_number_pos", "Move your mouse to the input field where you enter the purchase quantity and press 'X'.")
    ]

    # Update regions
    for section, key, description in regions:
        if section not in config:
            config[section] = {}
        config[section][key] = get_region(key, description)

    # Update positions
    for section, key, description in positions:
        if section not in config:
            config[section] = {}
        config[section][key] = get_position(key, description)

    # Automatically update screen resolution for full screen
    if "Imgur" not in config:
        config["Imgur"] = {}
    config["Imgur"]["fullscrean"] = get_screen_resolution()

    save_ini(config, ini_file)
    pyautogui.alert("All regions, positions, and screen resolution have been successfully saved!")

if __name__ == "__main__":
    main()
