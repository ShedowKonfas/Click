import telebot
import pyautogui
import time

text_chest = False

# Инициализация бота с токеном
bot = telebot.TeleBot("7501578133:AAGQPP1qEpBusawjZ7xt6CAXqd51a1EOdHs")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который может имитировать нажатия мыши. Используйте /help для начала.")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message, "Список команд: /start /help /click /press /type")

# Обработчик команды /click
@bot.message_handler(commands=['click'])
def click_mouse(message):
    bot.reply_to(message, "Начинаю имитировать нажатия мыши...")
    for _ in range(1):  # Количество нажатий
        pyautogui.click()  # Имитируем нажатие левой кнопки мыши
        #time.sleep(1)  # Задержка между нажатиями (1 секунда)
    bot.reply_to(message, "Имитирование нажатий завершено.")

# Обработчик команды /shutdown
#@bot.message_handler(commands=['shutdownn'])
#def press_hotkeys(message):
    #pyautogui.hotkey('win','r')
    #pyautogui.write("shutdown /s /t 2")
    #pyautogui.press("Enter")

# Обработчик команды /press
#@bot.message_handler(commands=['press'])
#def press_hotkeys(message):
    #pyautogui.hotkey('win','r')
    #pyautogui.write("shutdown /s /t 2000")
    #pyautogui.press("Enter")

# Обработчик команды /type
@bot.message_handler(commands=['type'])
def press_message(message):
    global text_chest
    text_chest = True
    bot.reply_to(message, "Какую фразу написать???")

@bot.message_handler(func=lambda message: True)
def type_text(message):
    global text_chest
    text_to_type=message.text
    time.sleep(2)
    pyautogui.write(text_to_type)
    text_chest = False

# Запуск бота
bot.polling()
