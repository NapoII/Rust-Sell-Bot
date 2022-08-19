py_name = "Rust - SellBot" 
v = "0.0.1"
####################################################################################################
# #   Intro

f0 =  """ 


- """ + py_name + """
- created by Napo_II
- """ + v + """
- python 2.7
- https://github.com/NapoII/

"""
print(" \nProgramm wird gestartet ...")

####################################################################################################
#import

from ast import While
from distutils.log import ERROR
import os
import os, sys
import time
import pyautogui
from Imports import*
import keyboard

################################################################################################################################
#PreSet Programm

file_path = os.path.dirname(sys.argv[0])
file_path_Bilder = file_path + "/Bilder/"
file_path_Work_Folder = file_path + "/Work_Folder/"


Doku_Folder = Folder_gen (py_name, "Documents/")
Log_Folder = Folder_gen ("Log", ("Documents/"+str(py_name)))
Log_File_name = Datei_name_mit_Zeit ("LogFile-"+str(py_name))
Log_File = Erstelle_TextDatei (Log_File_name, Log_Folder, f0 + "Log-File:\n---------------------------------------------------------------------------------------\n")

Bot_Path = os.path.dirname(sys.argv[0])
config_dir = file_path +"/config.ini"

log ( "Bot_Path: ["+str(Bot_Path) + "]\n")

print(f0)

################################################################################################################################
# Load Config

Knopf_Region = parse_int_tuple(read_config(config_dir, "ocv", "Knopf_Region"))
Shop_open_Region = parse_int_tuple(read_config(config_dir, "ocv", "Shop_open_Region"))
Inv_open_Region = parse_int_tuple(read_config(config_dir, "ocv", "Inv_Open_Region"))
ESC_Region = parse_int_tuple(read_config(config_dir, "ocv", "ESC_Region"))

Kaufknopf_pos = parse_int_tuple(read_config(config_dir, "Klick", "Kaufknopf_pos"))
Kaufknopf_anzahl_pos = parse_int_tuple(read_config(config_dir, "Klick", "Kaufknopf_anzahl_pos"))

max_Sec_to_wait = (read_config(config_dir, "Cheat_save", "max_Sec_to_wait"))
try:
    max_Sec_to_wait = int(max_Sec_to_wait)
except:
    max_Sec_to_wait = False

Bot_aktiv = read_config(config_dir, "Telegram", "Bot_aktiv")
CLINT_ID_imgur = read_config(config_dir, "Imgur", "CLINT_ID_imgur")
Telegram_token = read_config(config_dir, "Telegram", "Telegram_token")
chat_Id = read_config(config_dir, "Telegram", "chat_Id")
fullscrean = parse_int_tuple(read_config(config_dir, "Imgur", "fullscrean"))

OUT_OF_STOCK_Img_dir = file_path_Bilder + "/OUT_OF_STOCK.png"
CANT_AFFORD_Img_dir = file_path_Bilder + "/CANT_AFFORD.png"
BUY_Img_dir = file_path_Bilder + "/BUY.png"
Shop_open_Img_dir = file_path_Bilder + "/Shop_open.png"
Inv_open_Img_dir = file_path_Bilder + "/INV.png"
ESC_Img_dir = file_path_Bilder + "/ESC.png"

hotkey = pyautogui.prompt(text='HOTKEY um  den Sell zu Starten.', title=' X und Y Coredinate der Maus bestimmen' , default='ALt+E')
log("Der Hotkey wurde eingestellt auf: [ " + hotkey +" ]")

Scrap_start = int(pyautogui.prompt(text='Mit wie viel Scrap startest du?.', title='SELL BOT STATS' , default='0'))
Fert_start = int(pyautogui.prompt(text='Mit wie viel Fertilizer startest du?.', title='SELL BOT STATS' , default='1000'))


CANT_AFFORD = False
ERROR_No_Shop = False
ESC = False
Quit = False

################################################################################################################################
# Main Programm

if_Rust_aktiv()

print ("rdy ! ")
while True:
    if keyboard.is_pressed(hotkey):
        log("Sell Bot Start!")

        if Bot_aktiv == True:

            Screanshot_dir = Screanshot(fullscrean, "Rust - Screen_Start", file_path_Bilder)
            TeleBot_Say(f0 + "\n------------------------\n Rust - Sell Bot wurde gestartet.\nMit "+str(Fert_start)+" Fertilizer und "+ str(Scrap_start)+ " Scrap.", chat_Id, Telegram_token)
            TeleBot_img("Rust - Screen", Screanshot_dir, CLINT_ID_imgur, chat_Id, Telegram_token )
        
        log(f0 + "\n------------------------\n Rust - Sell Bot wurde gestartet.\nMit "+str(Fert_start)+" Fertilizer und "+ str(Scrap_start)+ " Scrap.")
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

                log ("Screanshot wurde an den Telebot gesendet.")
                Screanshot_dir = Screanshot(fullscrean, "Rust - Screen", file_path_Bilder)
                TeleBot_img("Rust - Screen", Screanshot_dir, CLINT_ID_imgur, chat_Id, Telegram_token )
                chat_date_id_ref = Last_chat_Data[2]

        else:
            pass

        if ERROR_No_Shop == True and ESC == False:
                
            log ("Etwas stimmt nicht. Schu mal nach!")
            if Bot_aktiv == True:
                Screanshot_dir = Screanshot(fullscrean, "Rust - Screen", file_path_Bilder)
                TeleBot_Say("Etwas stimmt nicht. Schu mal nach!", chat_Id, Telegram_token)
                TeleBot_img("Rust - Screen", Screanshot_dir, CLINT_ID_imgur, chat_Id, Telegram_token )
            Continue = pyautogui.confirm(text='Soll der Bot weiter machen?', title='Sell Bot', buttons=['Ja', 'Nein'])
            if Continue == "Ja":
                ERROR_No_Shop = False
                if_Rust_aktiv()
                pass
            else:
                Quit = True
                break

        while True:
            Shop_open = if_Shop_open(Shop_open_Img_dir, Shop_open_Region, 0.75)
            if Shop_open == True:
                break
            else:
                ESC = if_ESC(ESC_Img_dir, ESC_Region, 0.75)
                if ESC == True:
                    break
                X_Test = X_Test + 1
                if X_Test == 10:
                    ERROR_No_Shop = True
                    break
                Inv_open = if_Inv_open(Inv_open_Img_dir, Inv_open_Region, 0.75)
                if Shop_open == False and Inv_open == True:
                    pyautogui.press('Tab')
                    pyautogui.press('E')
                else:
                    pyautogui.press('E')
                    Shop_open = if_Shop_open(Shop_open_Img_dir, Shop_open_Region, 0.75)
                    if Shop_open == True:
                        break
        
        if CANT_AFFORD == True:
            time_y = time.time()
            time_ =  time_y - time_stemp

            Scrap_end = int(pyautogui.prompt(text='Mit wie viel Scrap hast du?.', title='SELL BOT STATS' , default='0'))
            Scrap_end = Scrap_end - Scrap_start

            Scrap_pro_sec = Scrap_end / time_
            Scrap_pro_min = Scrap_pro_sec / 60

            Fert_pro_sec = Fert_start / time_
            Fert_pro_min = Fert_pro_sec / 60
            
            stat_Card_Fert_text = "Es wurden "+str(Fert_start)+ " Fertilizer für " +str(Scrap_end) + " Scrap verkauft."
            stat_Card_Fert_text_len = len(stat_Card_Fert_text)

            stat_Card_Stat_text = str(Scrap_pro_min) +" Scrap/min.\n" + str(Fert_pro_min) +" Fertilizer/min."

            Card = stat_Card_Fert_text + "\n" + "-" * stat_Card_Fert_text_len + "\n" + stat_Card_Stat_text
            log("\n\n" + Card +"\n")
            TeleBot_Say(Card, chat_Id, Telegram_token)
            print("Done!")
            break

        while True:
            
            ESC = if_ESC(ESC_Img_dir, ESC_Region, 0.75)
            if ESC == True:
                log("ESC - Der Bot wurde Pausert.")
                time_y = time.time()
                time_ =  time_y - time_stemp

                Scrap_end = int(pyautogui.prompt(text='Mit wie viel Scrap hast du?.', title='SELL BOT STATS' , default='0'))
                Scrap_end = Scrap_end - Scrap_start

                Scrap_pro_sec = Scrap_end / time_
                Scrap_pro_min = Scrap_pro_sec / 60

                Fert_pro_sec = Fert_start / time_
                Fert_pro_min = Fert_pro_sec / 60
                
                stat_Card_Fert_text = "Es wurden "+str(Fert_start)+ " Fertilizer für " +str(Scrap_end) + " Scrap verkauft."
                stat_Card_Fert_text_len = len(stat_Card_Fert_text)

                stat_Card_Stat_text = str(Scrap_pro_min) +" Scrap/min.\n" + str(Fert_pro_min) +" Fertilizer/min."

                Card = stat_Card_Fert_text + "\n" + "-" * stat_Card_Fert_text_len + "\n" + stat_Card_Stat_text
                log("\n\n" + Card +"\n")
                if Bot_aktiv == True:
                    TeleBot_Say(Card, chat_Id, Telegram_token)
                Continue = pyautogui.confirm(text='Soll der Bot weiter machen?', title='Sell Bot', buttons=['Ja', 'Nein'])
                if Continue == "Ja":
                    if_Rust_aktiv()
                    pass
                else:
                    Quit = True
                    break

            CANT_AFFORD = if_CANT_AFFORD(CANT_AFFORD_Img_dir, Knopf_Region, 0.75)
            if CANT_AFFORD == True:
                log ("CANT_AFFORD - Alles Leer verkauft!")
                if Bot_aktiv == True:
                    Screanshot_dir = Screanshot(fullscrean, "Rust - Screen", file_path_Bilder)
                    TeleBot_Say("CANT_AFFORD - Alles Leer verkauft!!", chat_Id, Telegram_token)
                    TeleBot_img("CANT_AFFORD - Alles Leer verkauft!", Screanshot_dir, CLINT_ID_imgur, chat_Id, Telegram_token )
                
                break

            Buy = if_BUY(BUY_Img_dir, Knopf_Region, 0.75)
            if Buy == True:

                Random_num = (random.uniform(0.1, 0.3))
                if max_Sec_to_wait == False:
                    Random_num = 0.01

                pyautogui.moveTo(Kaufknopf_anzahl_pos[0], Kaufknopf_anzahl_pos[1], Random_num, pyautogui.easeInQuad)
                pyautogui.click()
                pyautogui.write('99', interval=0.25)
                pyautogui.moveTo(Kaufknopf_pos[0], Kaufknopf_pos [1], Random_num, pyautogui.easeInQuad)
                pyautogui.click()
                Zeit_pause(1)
                pyautogui.moveTo(1835+(random.randrange(10)), 830+(random.randrange(10)), Random_num, pyautogui.easeInBounce)

            if max_Sec_to_wait == False:
                pass
            else:
                random_num = (random.randrange(max_Sec_to_wait))+1
                log ( "\nBot save Stop für "+str(random_num)+" sec")
                Bar(random_num*10)
                break
