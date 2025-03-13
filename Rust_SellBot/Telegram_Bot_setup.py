################################################################################################################################
# Telegram_Bot_einrichten.py
from util.__funktion__ import *
import webbrowser
import os
webbrowser.open("https://core.telegram.org/bots#3-how-do-i-create-a-bot")
pyautogui.alert(text='First you have to create a Telegram bot\nand copy the token of your bot!', title='Rust - SellBot - Telegram Set-Up', button='Lets Go!')

file_path = os.path.normpath(os.path.dirname(sys.argv[0]))
file_path_img = os.path.normpath(os.path.join(file_path, "img"))
config_dir = os.path.normpath(os.path.join(file_path,"cfg","config.ini"))
config_token_dir = os.path.normpath(os.path.join(file_path,"cfg","token.ini"))

Token = pyautogui.prompt(text='Enter the Telegram Bot Token here:', title='Rust - SellBot - Telegram Set-Up' , default='5357034455:AAE785813q8L1np9oBoq0S6Vmyr9MB2F_oU')
Telegram_token = Token
write_config(config_token_dir, "Telegram", "Telegramm_token", str(Token))

pyautogui.alert(text='Write your Telegram Bot now with: !id . Then press "Next" here". ', title='Rust - SellBot - Telegram Set-Up', button='Continue')

while True:
    try:
        Last_Chat_data = Last_Chat(Telegram_token)
    except:
        while True:
            pyautogui.alert(text='Write your Telegram Bot now with: !id . Then press " Continue " here. ', title='Rust - SellBot - Telegram Set-Up', button='Continue')
            Last_Chat_data = Last_Chat(Telegram_token)
    if Last_Chat_data[0].lower() == "" or Last_Chat_data[0].lower() != "!id":
        pyautogui.alert(text='Write your Telegram Bot now with: !id . Then press " Continue " here.', title='Rust - SellBot - Telegram Set-Up', button='Continue')
        Last_Chat_data = Last_Chat(Telegram_token)

    if Last_Chat_data[0].lower() == "!id":
        log ("\nID found!\n")
        break

Chat_ID =(Last_Chat_data[1])
write_config(config_dir, "Telegram", "chat_Id", str(Chat_ID))

webbrowser.open("https://imgur.com/account/settings/apps")
pyautogui.alert(text='Now create an Imgur token. ', title='Rust - SellBot - Telegram Set-Up', button='Continue')

CLINT_ID_imgur = pyautogui.prompt(text='Gib die Imgur Client ID hier ein:', title='Rust - SellBot - Telegram Set-Up' , default='fb9b5757ec16f06')
CLINT_Secret_imgur = pyautogui.prompt(text='Gib den Imgur Client Secret hier ein:', title='Rust - SellBot - Telegram Set-Up' , default='c8eadb8777f5bbebf4c408fa039420e18e153cc8')


write_config(config_token_dir, "Imgur", "CLINT_ID_imgur", str(CLINT_ID_imgur))
write_config(config_token_dir, "Imgur", "CLINT_Secret_imgur", str(CLINT_Secret_imgur))


pyautogui.alert(text='The Telegram Bot has been set up. ', title='Rust - SellBot - Telegram Set-Up', button='Continue')

TeleBot_Say("Done the Telegram bot has been set up.\n write /scr to test the image functionality.", Chat_ID, Token)
chat_date_id = 0
chat_date_id_ref = 1

fullscrean = read_config(config_dir, "Imgur", "fullscrean", "tuple")

while True:
    Last_chat_Data = Last_Chat(Telegram_token)

    if Last_chat_Data[0].lower() == "/scr" and chat_date_id != chat_date_id_ref:

        log ("Screanshot was sent to the Telebot.")
        Screanshot_dir = Screanshot(fullscrean, "Rust - Screen", file_path_img)
        TeleBot_img("Rust - Screen", Screanshot_dir, CLINT_ID_imgur, Chat_ID, Telegram_token )
        chat_date_id_ref = Last_chat_Data[2]
        break
    else:
        TeleBot_Say("Now write /scr in the Telegram chat to test the picture function! ", Chat_ID, Token)
        pyautogui.alert(text='Now write /scr in the Telegram chat to test the picture function! ', title='Rust - SellBot - Telegram Set-Up', button='Continue')


TeleBot_Say("The Telegram Bot is ready for use for the Rust Sell Bot", Chat_ID, Token)
write_config(config_dir, "Telegram", "Bot_aktiv", "True")
pyautogui.alert(text='Done!. ', title='Rust - SellBot - Telegram Set-Up', button='Continue')






