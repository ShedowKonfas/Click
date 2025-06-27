import telebot
import pyautogui
import time

# Инициализация бота с токеном
bot = telebot.TeleBot("7501578133:AAGQPP1qEpBusawjZ7xt6CAXqd51a1EOdHs")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который может имитировать нажатия мыши. Используйте /click для начала.")

# Обработчик команды /click
@bot.message_handler(commands=['click'])
def click_mouse(message):
    bot.reply_to(message, "Начинаю имитировать нажатия мыши...")
    for _ in range(1):  # Количество нажатий
        pyautogui.click()  # Имитируем нажатие левой кнопки мыши
        time.sleep(1)  # Задержка между нажатиями (1 секунда)
    bot.reply_to(message, "Имитирование нажатий завершено.")

# Запуск бота
bot.polling()
