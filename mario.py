from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Telegram Bot token'ınızı buraya girin
TOKEN = '7530787302:AAHXfYHtnGiVK9RVsqUlL1twb0Kyq-1Wvrw'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Super Mario Coin Collector Oyna", callback_data='play')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Hoş geldiniz! Oynamak için aşağıdaki butona tıklayın.", reply_markup=reply_markup)

async def play_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # HTML5 oyununuzun barındırıldığı URL
    game_url = 'https://github.com/adigozal/MarioTeleBot.git'
    
    # Kullanıcıya oyun URL'sini gönderiyoruz
    await query.message.reply_game("MarioTeleBot", game_url)

def main() -> None:
    # Bot uygulamasını oluşturun ve bot token'ı girin
    app = Application.builder().token(TOKEN).build()

    # Handler'ları ekleyin
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(play_game, pattern='^play$'))

    # Botu çalıştırın
    app.run_polling()

if __name__ == '__main__':
    main()