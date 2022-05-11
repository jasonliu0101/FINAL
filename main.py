import traceback

from flask import Flask, request, abort
from linebot import(
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import(
    MessageEvent, TextMessage, TextSendMessage, SourceUser
)

import reply_console

# [CHANGE-WITH-YOUR-BOT-PROFILES] link-to-bot backend configuration variables
channel_access_token = 'OLBdIZ4fk4T1Di+1/282O4XTq9QnW2PaebSWnWKB9aep4UaVJviuOhxX57lAMOF2pMf39u/0jeFPmesK0zG/jZTN6GCe02wmj66f9jMJ9FAuAeyRarkyMdIQfuEqZ+3kD0oaHfzQedT7nGKx2G9fsgdB04t89/1O/w1cDnyilFU='
channel_secret = '2195e23ba32d82c498ec8b5ff429e7d4'


# initialize and callback
app = Flask(__name__)
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: "+ body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Check Access Token or Channel Secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
        try:
            UserID = event.source.user_id
            user_display_name = line_bot_api.get_profile(UserID).display_name  #獲得使用者的名稱
            line_bot_api.reply_message(
                event.reply_token,
                reply_console.reply(event.message.text,user_display_name)  #呼叫reply_console裡面的reply()，接下來給reply_console裡的reply()處理
            )
        except AttributeError:
            print(event.message.text)
            print("Not Fit")
        except:
            line_bot_api.reply_message(
                event.reply_token,
                reply_console.reply("Error")
            )
            print(traceback.format_exc())

if __name__ == "__main__":
    app.run()









