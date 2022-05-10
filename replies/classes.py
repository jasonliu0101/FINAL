from linebot.models import *

class_dict = {
    "我要選課！",
    "選課查詢",
    "單科加選",
    "棄選流程",
    "通識登記一",
    "通識登記二"
}


def reply(input):
    if input == "我要選課！":
        return [TextSendMessage(text="選課小幫手，請選擇要需要教學的選課流程"),
                TemplateSendMessage(  # 這個是按鈕樣版訊息的格式
                    alt_text="template",
                    template=ButtonsTemplate(
                        title="請選擇",
                        text="👇",
                        actions=[
                            MessageAction(  # 這邊是在設定按鈕按下以後回傳的是訊息
                                label="選課查詢",
                                text="選課查詢",
                            ),
                            MessageAction(
                                label="單科加選",
                                text="單科加選"
                            ),
                            MessageAction(
                                label="棄選流程",
                                text="棄選流程",
                            ),
                            MessageAction(
                                label="通識登記一",
                                text="通識登記一"
                            ),
                            # MessageAction(
                            #     label="通識登記二",
                            #     text="通識登記二"
                            # )
                        ]

                    )
                )
                ]

    elif input == "選課查詢":
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
