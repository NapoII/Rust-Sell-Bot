"""Full Doku on: https://github.com/NapoII/Rust - SellBot"
-----------------------------------------------
!!! ADD MUST HAVE INFO !!
------------------------------------------------
"""

# import

import pyautogui
import keyboard
import time
import os
import random
import sys

from util.__funktion__ import *

py_name = "Rust - SellBot"
v = "1.0.2"
####################################################################################################
# #   Intro

f0 = """


- """ + py_name + """
- created by Napo_II
- """ + v + """
- python 3.12
- https://github.com/NapoII/Rust-Sell-Bot

"""
log(" \nProgramme is started ...")

####################################################################################################
# import


################################################################################################################################
# PreSet Programm

file_path = os.path.dirname(sys.argv[0])
file_path_img = os.path.join(file_path, "img")

config_dir = os.path.join(file_path, "cfg", "config.ini")
config_token_dir = os.path.join(file_path, "cfg", "token.ini")

Bot_Path = os.path.dirname(sys.argv[0])

log(f"Bot_Path: [{Bot_Path}]\n")

print(f0)

################################################################################################################################
# Load Config

button_region = read_config(config_dir, "ocv", "button_region", "tuple")
shop_open_region = read_config(config_dir, "ocv", "shop_open_region", "tuple")
inv_open_region = read_config(config_dir, "ocv", "inv_open_region", "tuple")
esc_region = read_config(config_dir, "ocv", "esc_region", "tuple")

buy_button_pos = read_config(config_dir, "Klick", "buy_button_pos", "tuple")
buy_button_number_pos = read_config(
    config_dir, "Klick", "buy_button_number_pos", "tuple")

max_Sec_to_wait = read_config(config_dir, "Cheat_save", "max_Sec_to_wait")
try:
    max_Sec_to_wait = int(max_Sec_to_wait)
except:
    max_Sec_to_wait = False

Bot_aktiv = str_to_bool(read_config(config_dir, "Telegram", "Bot_aktiv"))
CLINT_ID_imgur = read_config(config_token_dir, "Imgur", "CLINT_ID_imgur")
Telegram_token = read_config(config_token_dir, "Telegram", "Telegram_token")
chat_Id = read_config(config_dir, "Telegram", "chat_Id")
fullscrean = read_config(config_dir, "Imgur", "fullscrean", "tuple")


OUT_OF_STOCK_Img_dir = os.path.join(file_path_img, "OUT_OF_STOCK.png")
CANT_AFFORD_Img_dir = os.path.join(file_path_img, "CANT_AFFORD.png")
BUY_Img_dir = os.path.join(file_path_img, "BUY.png")
Shop_open_Img_dir = os.path.join(file_path_img, "Shop_open.png")
Inv_open_Img_dir = os.path.join(file_path_img, "INV.png")
ESC_Img_dir = os.path.join(file_path_img, "ESC.png")

hotkey = pyautogui.prompt(text='HOTKEY to start the Sellbot.',
                          title=' Determine X and Y coredinates of the mouse', default='ALt+E')
log(f"The hotkey was set to: [ {hotkey} ]")

Scrap_start = int(pyautogui.prompt(
    text='How much scrap do you start with?.', title='SELL BOT STATS', default='0'))
Fert_start = int(pyautogui.prompt(
    text='How much Fertilizer do you start with?.', title='SELL BOT STATS', default='1000'))


CANT_AFFORD = False
ERROR_No_Shop = False
ESC = False
Quit = False

################################################################################################################################
# Main Programm

if_Rust_aktiv()

log(f"Bot is ready to start with the HotKey: {hotkey}")

while True:
    if keyboard.is_pressed(hotkey):
        log("Sell Bot Start!")

        if Bot_aktiv == True:

            Screanshot_dir = Screanshot(
                fullscrean, "Rust - Screen_Start", file_path_img)
            TeleBot_Say(
                f"{f0}\n------------------------\nRust - Sell Bot was launched.\nWith {Fert_start} Fertilizer and {Scrap_start} Scrap.", chat_Id, Telegram_token)
            TeleBot_img("Rust - Screen", Screanshot_dir,
                        CLINT_ID_imgur, chat_Id, Telegram_token)

        log(f"{f0}\n------------------------\n Rust - Sell Bot was launched.\nWith {Fert_start} Fertilizer and {Scrap_start} Scrap.")
        time_stemp = time.time()
        break

chat_date_id = 0
chat_date_id_ref = 1
while True:
    if Quit == True:
        break

    X_Test = 0

    if Bot_aktiv == True:
        Last_chat_Data = Last_Chat(Telegram_token)
        chat_date_id = Last_chat_Data[2]

        if Last_chat_Data[0] == "/scr" and chat_date_id != chat_date_id_ref:

            log("Screanshot was sent to the Telebot.")
            Screanshot_dir = Screanshot(
                fullscrean, "Rust - Screen", file_path_img)
            TeleBot_img("Rust - Screen", Screanshot_dir,
                        CLINT_ID_imgur, chat_Id, Telegram_token)
            chat_date_id_ref = Last_chat_Data[2]

    else:
        pass

    if ERROR_No_Shop == True and ESC == False:

        log("Something is wrong. Check it out!")
        if Bot_aktiv == True:
            Screanshot_dir = Screanshot(
                fullscrean, "Rust - Screen", file_path_img)
            TeleBot_Say("Something is wrong. Check it out!",
                        chat_Id, Telegram_token)
            TeleBot_img("Rust - Screen", Screanshot_dir,
                        CLINT_ID_imgur, chat_Id, Telegram_token)
        Continue = pyautogui.confirm(
            text='Should the bot continue?', title='Sell Bot', buttons=['Yes', 'No'])
        if Continue == "Yes":
            ERROR_No_Shop = False
            if_Rust_aktiv()
            pass
        else:
            Quit = True
            break
    while True:
        Shop_open = if_img(Shop_open_Img_dir,
                           shop_open_region, 0.75, "Shop_open")
        if Shop_open == True:
            break
        else:
            ESC = if_img(ESC_Img_dir, esc_region, 0.75, "ESC")
            if ESC == True:
                break
            X_Test = X_Test + 1
            if X_Test == 10:
                ERROR_No_Shop = True
                break
            Inv_open = if_img(Inv_open_Img_dir,
                              inv_open_region, 0.75, "Inv_open")
            if Shop_open == False and Inv_open == True:
                pyautogui.press('Tab')
                pyautogui.press('E')
                log(f"pressing TAB, E")
            else:
                pyautogui.press('E')
                log(f"pressing E")
                Shop_open = if_img(Shop_open_Img_dir,
                                   shop_open_region, 0.75, "Shop_open")
                if Shop_open == True:
                    break

    if CANT_AFFORD == True:
        time_y = time.time()
        time_ = time_y - time_stemp

        Scrap_end = int(pyautogui.prompt(
            text='How much scrap did you use?.', title='SELL BOT STATS', default='0'))
        Scrap_end = Scrap_end - Scrap_start

        Scrap_pro_sec = Scrap_end / time_
        Scrap_pro_min = Scrap_pro_sec / 60

        Fert_pro_sec = Fert_start / time_
        Fert_pro_min = Fert_pro_sec / 60

        stat_Card_Fert_text = f"There were {Fert_start} Fertilizer for {Scrap_end} Scrap sold."
        stat_Card_Fert_text_len = len(stat_Card_Fert_text)

        stat_Card_Stat_text = f"{Scrap_pro_min}  Scrap/min.\n {Fert_pro_min} Fertilizer/min."
        Separation_line = "-" * stat_Card_Fert_text_len
        Card = f"{stat_Card_Fert_text}\n{Separation_line}\n{stat_Card_Stat_text}"
        log(f"\n\n{Card}\n")
        TeleBot_Say(Card, chat_Id, Telegram_token)
        log("Done!")
        break

    while True:

        ESC = if_img(ESC_Img_dir, esc_region, 0.75, "ESC")
        if ESC == True:
            log("ESC - The bot was paused.")
            time_y = time.time()
            time_ = time_y - time_stemp

            Scrap_end = int(pyautogui.prompt(
                text='How much scrap did you use?.', title='SELL BOT STATS', default='0'))
            Scrap_end = Scrap_end - Scrap_start

            Scrap_pro_sec = Scrap_end / time_
            Scrap_pro_min = Scrap_pro_sec / 60

            Fert_pro_sec = Fert_start / time_
            Fert_pro_min = Fert_pro_sec / 60

            stat_Card_Fert_text = f"There were {Fert_start} Fertilizer for {Scrap_end} Scrap sells."
            stat_Card_Fert_text_len = len(stat_Card_Fert_text)

            stat_Card_Stat_text = f"{Scrap_pro_min} Scrap/min.\n {Fert_pro_min} Fertilizer/min."
            Separation_line = "-" * stat_Card_Fert_text_len

            Card = f"{stat_Card_Fert_text}\n{Separation_line}\n{stat_Card_Stat_text}"
            log(f"\n\n{Card}\n")
            if Bot_aktiv == True:
                TeleBot_Say(Card, chat_Id, Telegram_token)
            Continue = pyautogui.confirm(
                text='Should the bot continue?', title='Sell Bot', buttons=['Yes', 'No'])
            if Continue == "Yes":
                if_Rust_aktiv()
                pass
            else:
                Quit = True
                break

        CANT_AFFORD = if_img(CANT_AFFORD_Img_dir,
                             button_region, 0.75, "CANT_AFFORD")
        if CANT_AFFORD == True:
            log("CANT_AFFORD - Everything Empty Sold!")
            if Bot_aktiv == True:
                Screanshot_dir = Screanshot(
                    fullscrean, "Rust - Screen", file_path_img)
                TeleBot_Say("CANT_AFFORD - All sold empty!!!",
                            chat_Id, Telegram_token)
                TeleBot_img("CANT_AFFORD - All sold empty!!!",
                            Screanshot_dir, CLINT_ID_imgur, chat_Id, Telegram_token)

            break

        Buy = if_img(BUY_Img_dir, button_region, 0.75, "Buy")
        if Buy == True:

            Random_num = (random.uniform(0.1, 0.3))
            if max_Sec_to_wait == False:
                Random_num = 0.01

            pyautogui.moveTo(
                buy_button_number_pos[0], buy_button_number_pos[1], Random_num, pyautogui.easeInQuad)
            pyautogui.click()
            pyautogui.write('99', interval=0.25)
            pyautogui.moveTo(
                buy_button_pos[0], buy_button_pos[1], Random_num, pyautogui.easeInQuad)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1835+(random.randrange(10)), 830 +
                             (random.randrange(10)), Random_num, pyautogui.easeInBounce)

        if max_Sec_to_wait == False:
            break
        else:
            random_num = (random.randrange(max_Sec_to_wait))+1
            log("\nBot save Stop for "+str(random_num)+" sec")
            Bar(random_num*10)
            break
