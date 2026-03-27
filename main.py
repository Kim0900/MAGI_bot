import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# 서버가 살아있는지 확인하는 용도 (Render용)
app = Flask('')
@app.route('/')
def home(): return "System Alive"

def run_flask():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

# 사진을 받았을 때 실행할 내용
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ 서버에서 콜카드를 정상적으로 수신했습니다!")

if __name__ == '__main__':
    Thread(target=run_flask).start() # 웹 서버 시작
    
    # TELEGRAM_TOKEN은 나중에 Render 설정에서 입력할 거예요.
    token = os.environ.get('TELEGRAM_TOKEN')
    application = ApplicationBuilder().token(token).build()
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    
    application.run_polling()
