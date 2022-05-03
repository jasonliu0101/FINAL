from linebot.models import *

food_dict = { #本頁所有的回應，從這邊判斷而不從if-else判斷是因為dict比較快
    "找吃的！",
    "早餐！",
    "百元內正餐！",
    "百元以上正餐！",
    "甜點！"
}


def reply(input,username):
    if input == "找吃的！":
        return find_eat()
    elif input == "早餐！":
        return return_meal("breakfast")
    elif input == "百元內正餐！":
        return return_meal("lunch")
    elif input == "百元以上正餐":
        return return_meal("dinner")
    elif input == "甜點！":
        return return_meal("night_supper")


def find_eat():
    return TextSendMessage(    #TextSendMessage:傳訊息，quick_reply：訊息下面的快速按鈕
        text="在找什麼類型的美食呢？",
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(action=MessageAction(label="早餐", text="早餐！")),   #QuickReplyButton:設定按鈕的內容
                QuickReplyButton(action=MessageAction(label="百元內正餐", text="百元內正餐！")),
                QuickReplyButton(action=MessageAction(label="百元以上正餐", text="百元以上正餐！")),
                QuickReplyButton(action=MessageAction(label="甜點", text="甜點！"))
            ])
    )

def return_meal(meal):
    if meal == "breakfast":
        return [TextSendMessage(text="這邊是成大周邊的美食早點，快挑一家嚐嚐吧🤤🤤"),
                ImageSendMessage(original_content_url='https://imgur.com/Nw2KB08.jepg',
                                 preview_image_url='https://imgur.com/Nw2KB08.jpeg',

                                 original_content_url='https://imgur.com/4MBTEI6.jpeg',
                                 preview_image_url='https://imgur.com/4MBTEI6.jpeg',
                                ),
                                 ]

    elif meal == "lunch":
        return [TextSendMessage(text="齁齁這是成大周邊的百元內正餐，俗又大碗啦🤤🤤"),
                ImageSendMessage(original_content_url='https://imgur.com/jdoJL4U.jepg',
                                 preview_image_url='https://imgur.com/jdoJL4U.jpeg',

                                 original_content_url='https://imgur.com/TBd7cEJ.jpeg',
                                 preview_image_url='https://imgur.com/TBd7cEJ.jpeg',

                                 original_content_url='https://imgur.com/YGbD0ZX.jpeg',
                                 preview_image_url='https://imgur.com/YGbD0ZX.jpeg',

                                 original_content_url='https://imgur.com/MwevHNa.jpeg',
                                 preview_image_url='https://imgur.com/MwevHNa.jpeg',
                                ),
                                 ]
    elif meal == "dinner":
        return [TextSendMessage(text="想要犒賞自己嗎？百元以上正餐在這裡～🥺🥺"),
                ImageSendMessage(original_content_url='https://imgur.com/qcHq4KX.jepg',
                                 preview_image_url='https://imgur.com/qcHq4KX.jpeg',

                                 original_content_url='https://imgur.com/KLFdjXL.jpeg',
                                 preview_image_url='https://imgur.com/KLFdjXL.jpeg',

                                 original_content_url='https://imgur.com/cNKNN9B.jpeg',
                                 preview_image_url='https://imgur.com/cNKNN9B.jpeg',

                                 original_content_url='https://imgur.com/QC9ISoa.jpeg',
                                 preview_image_url='https://imgur.com/QC9ISoa.jpeg',
                                ),
                                 ]
    elif meal == "night_supper":
        return [TextSendMessage(text="來台南94要吃甜點～～🥺🥺"),
                ImageSendMessage(original_content_url='https://imgur.com/iaJQ92J.jepg',
                                 preview_image_url='https://imgur.com/iaJQ92J.jpeg',

                                 original_content_url='https://imgur.com/O5pa1fK.jpeg',
                                 preview_image_url='https://imgur.com/O5pa1fK.jpeg',

                                 original_content_url='https://imgur.com/d3BHhvF.jpeg',
                                 preview_image_url='https://imgur.com/d3BHhvF.jpeg',

                                 original_content_url='https://imgur.com/sU9yxSU.jpeg',
                                 preview_image_url='https://imgur.com/sU9yxSU.jpeg',

                                 original_content_url='https://imgur.com/eAKXEPi.jpeg',
                                 preview_image_url='https://imgur.com/eAKXEPi.jpeg',
                                ),
                                 ]

