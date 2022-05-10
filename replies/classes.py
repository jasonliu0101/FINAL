from linebot.models import *

class_dict = {
    "選課查詢",
    "單科加選",
    "棄選流程",
    "通識登記一",
    "通識登記二"
}


def reply(input):
    if input == "選課查詢":
        return [ImageSendMessage(original_content_url='https://i.imgur.com/Y3DKI9C.jpeg',
                                 preview_image_url='https://i.imgur.com/Y3DKI9C.jpeg')]

    elif input == "單科加選":
        return [ImageSendMessage(original_content_url='https://i.imgur.com/rsB1MEZ.jpeg',
                                 preview_image_url='https://i.imgur.com/rsB1MEZ.jpeg')]

    elif input == "棄選流程":
        return [ImageSendMessage(original_content_url='https://i.imgur.com/P9PES7z.jpeg',
                                 preview_image_url='https://i.imgur.com/P9PES7z.jpeg')]

    elif input == "通識登記一":
        return [ImageSendMessage(original_content_url='https://i.imgur.com/gUttt07.jpeg',
                                 preview_image_url='https://i.imgur.com/gUttt07.jpeg')]

    elif input == "通識登記二":
        return [ImageSendMessage(original_content_url='https://i.imgur.com/AEnaRAZ.jpeg',
                                 preview_image_url='https://i.imgur.com/AEnaRAZ.jpeg')]
