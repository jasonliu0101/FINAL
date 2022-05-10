#功能區
@handler.add(MessageEvent, message=TextMessage) 
def handle_message(event):
    message =event.message.text               #取得使用者訊息
    if re.match('選課查詢',message):
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/Y3DKI9C.jpeg',
            preview_image_url='https://i.imgur.com/Y3DKI9C.jpeg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    elif re.match('單科加選',message):
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/rsB1MEZ.jpeg',
            preview_image_url='https://i.imgur.com/rsB1MEZ.jpeg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)   
    elif re.match('棄選流程',message):
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/P9PES7z.jpeg',
            preview_image_url='https://i.imgur.com/P9PES7z.jpeg'
        )
        line_bot_api.reply_message(event.reply_token, image_message) 
    elif re.match('通識登記一',message):
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/gUttt07.jpeg',
            preview_image_url='https://i.imgur.com/gUttt07.jpeg'
        )
        line_bot_api.reply_message(event.reply_token, image_message) 
    elif re.match('通識登記二',message):
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/AEnaRAZ.jpeg',
            preview_image_url='https://i.imgur.com/AEnaRAZ.jpeg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)     

    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))





if __name__ == '__main__':
    app.run("0.0.0.0")      
