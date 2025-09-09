import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("AAFqz0KK86gyz6N5D_1dWC5D7r9mUZArlfc")
WEATHER_API_KEY = os.getenv("33550388fb984ac5936151043250909")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши /weather <город>")

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Укажи город. Пример: /weather Almaty")
        return
    city = " ".join(context.args)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    r = requests.get(url).json()

    if r.get("main"):
        temp = r["main"]["temp"]
        desc = r["weather"][0]["description"]
        await update.message.reply_text(f"Погода в {city}: {temp}°C, {desc}")
    else:
        await update.message.reply_text("Город не найден!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weather", weather))
    app.run_polling()

if __name__ == "__main__":
    main()
