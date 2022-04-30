import traceback

from flask import Flask, request, abort
from linebot import(
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import(
    MessageEvent, TextMessage, TextSendMessage
)

import reply_console

# [CHANGE-WITH-YOUR-BOT-PROFILES] link-to-bot backend configuration variables
channel_access_token = 'ly2CDt7pMiUZuG/9ZA0NvusP0846dHLu0CMGUTe7zUGaZ1AgE7J9EdvIoNB7UHqLH56/ruq8XvtyeBQv/hYeR+NS/0YNYvEtMTnp5jlZlY39rPmYfRnUuLBWyMUo1HKK+/VPPshE3A3kT4M3QDVkQgdB04t89/1O/w1cDnyilFU='
channel_secret = 'f35fa7ced6a3e64f9e066f3f454951af'


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
            line_bot_api.reply_message(
                event.reply_token,
                reply_console.reply(event.message.text)
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









