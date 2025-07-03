import telebot
import pyautogui
import time
import random

text_chest = False
hotkey_chest = False

hype_rand = ["HYPE!!!-Legendary", "hype-epic", "hype-rare"]
probabilities = [0.05, 0.3, 0.65]  # Сумма 1 (5%, 30%, 65%)
result = random.choices(hype_rand, weights=probabilities, k=1)[0]


# Инициализация бота с токеном
bot = telebot.TeleBot("your_token_bot")

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
        # time.sleep(1)  # Задержка между нажатиями (1 секунда)
    bot.reply_to(message, "Имитирование нажатий завершено.")

# Обработчик команды /shutdown
@bot.message_handler(commands=['shutdown', "sh"])
def shutdown(message):
    bot.reply_to(message, "Я устал Босс...")
    pyautogui.hotkey('win', 'r')
    pyautogui.write("shutdown /s /t 120")
    pyautogui.press("Enter")

# Обработчик команды /press
@bot.message_handler(commands=['press'])
def press_hotkeys(message):
    global hotkey_chest
    hotkey_chest = True
    bot.reply_to(message, "Какую комбинацию клавиш нажать? Пример: win r")

# Обработчик команды /type
@bot.message_handler(commands=['type'])
def type_message(message):
    global text_chest
    text_chest = True
    bot.reply_to(message, "Какую фразу написать?")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    global text_chest, hotkey_chest

    if hotkey_chest:
        hotkey_to_press = message.text.split()  # Разделяем строку на отдельные клавиши
        time.sleep(2)
        pyautogui.hotkey(*hotkey_to_press)  # Используем распаковку аргументов
        hotkey_chest = False
        bot.reply_to(message, "Комбинация клавиш нажата.")

    elif text_chest:
        text_to_type = message.text
        time.sleep(2)
        pyautogui.write(text_to_type)
        text_chest = False
        bot.reply_to(message, "Фраза написана.")


# Обработчик стикеров
@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    bot.reply_to(message, result)

# Запуск бота
bot.polling()
