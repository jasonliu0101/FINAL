from linebot.models import *

dorm_dict = {
    "找宿舍！",
    "我是男生！",
    "我是女生！",
    "我是便利商店愛好者",
    "一樣有便利商店但設備較新的",
    "我怕吃土，給我最便宜的",
    "讓我看看最豪華的選項吧！",
    "想要雙人房",
    "我愛三人房",
    "給我套房！",
    "木製傢俱我的愛"
}


def reply(input, username):
    if input == "找宿舍！":
        return choose_sex(username)

    elif input == "我是男生！":
        return choose_dorm("man")

    elif input == "我是女生！":
        return choose_dorm("woman")

    elif input == "想要雙人房":
        return get_dorm_result_woman(input)

    elif input == "我愛三人房":
        return get_dorm_result_woman(input)

    elif input == "給我套房！":
        return get_dorm_result_woman(input)

    elif input == "木製傢俱我的愛":
        return get_dorm_result_woman(input)

    elif input == "我是便利商店愛好者":
        return get_dorm_result_man(input)

    elif input == "一樣有便利商店但設備較新的":
        return get_dorm_result_man(input)

    elif input == "我怕吃土，給我最便宜的":
        return get_dorm_result_man(input)

    elif input == "讓我看看最豪華的選項吧！":
        return get_dorm_result_man(input)

def choose_sex(username):
    return [TextSendMessage(
        text="哈囉" + username + "，在找宿舍嗎？\n宿舍生活絕對是大學青春生涯的第一步！祝福你遇見好室友😍😍"),
        TextSendMessage(
            text="那請問你是男生還是女生呢？",
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(action=MessageAction(label="男生", text="我是男生！")),
                    QuickReplyButton(action=MessageAction(label="女生", text="我是女生！"))
                ])
        )]


def choose_dorm(sex):
    emoji = [
        line_emoji_x1(2, "5ac1bfd5040ab15980c9b435", "020"),
        line_emoji_x1(30, "5ac1bfd5040ab15980c9b435", "003"),
        line_emoji_x1(31, "5ac1bfd5040ab15980c9b435", "003"),
    ]
    if sex == "man":
        return [
            TextSendMessage(text="讚讚$！那這是成大四間宿舍的外觀圖，有沒有特別想要的偏好呢？$$", emojis=emoji),
            TemplateSendMessage(
                alt_text="template",
                template=ButtonsTemplate(
                    thumbnail_image_url="https://i.imgur.com/JXTwuZw.jpeg",
                    title="選一個偏好吧！",
                    text="👇",
                    actions=[
                        MessageAction(
                            label="我是便利商店愛好者",
                            text="我是便利商店愛好者",
                        ),
                        MessageAction(
                            label="一樣有便利商店但設備較新的",
                            text="一樣有便利商店但設備較新的"
                        ),
                        MessageAction(
                            label="我怕吃土，給我最便宜的",
                            text="我怕吃土，給我最便宜的",
                        ),
                        MessageAction(
                            label="讓我看看最豪華的選項吧！",
                            text="讓我看看最豪華的選項吧！"
                        )
                    ]

                )
            )
        ]
    elif sex == "woman":
        return [
            TextSendMessage(text="讚讚$！那這是成大四間宿舍的外觀圖，有沒有特別想要的偏好呢？$$", emojis=emoji),
            TemplateSendMessage(
                alt_text="template",
                template=ButtonsTemplate(
                    thumbnail_image_url="https://i.imgur.com/llOZodk.jpeg",
                    title="選一個偏好吧！",
                    text="👇",
                    actions=[
                        MessageAction(
                            label="想要雙人房",
                            text="想要雙人房",
                        ),
                        MessageAction(
                            label="我愛三人房",
                            text="我愛三人房"
                        ),
                        MessageAction(
                            label="給我套房！",
                            text="給我套房！",
                        ),
                        MessageAction(
                            label="木製傢俱我的愛",
                            text="木製傢俱我的愛"
                        )
                    ]

                )
            )
        ]


def get_dorm_result_man(input):
    if input == "我怕吃土，給我最便宜的":
        return [TextSendMessage(text="看來最適合你的是【勝一】"),
                ImageSendMessage(original_content_url='https://i.imgur.com/X6fPDEi.jpeg',
                                 preview_image_url='https://i.imgur.com/X6fPDEi.jpeg'),
                TextSendMessage(text="除了這邊的懶人包以外網路上也有很多資訊喔～祝福你抽到最適合你的宿舍！🥺🥺")]

    elif input == "我是便利商店愛好者":
        return [TextSendMessage(text="看來最適合你的是【光一】"),
                ImageSendMessage(original_content_url='https://i.imgur.com/ztLc7oS.jpeg',
                                 preview_image_url='https://i.imgur.com/ztLc7oS.jpeg'),
                TextSendMessage(text="除了這邊的懶人包以外網路上也有很多資訊喔～祝福你抽到最適合你的宿舍！🥺🥺")]
    elif input == "一樣有便利商店但設備較新的":
        return [TextSendMessage(text="看來最適合你的是【光二】"),
                ImageSendMessage(original_content_url='https://i.imgur.com/lu1ckVy.jpeg',
                                 preview_image_url='https://i.imgur.com/lu1ckVy.jpeg'),
                TextSendMessage(text="除了這邊的懶人包以外網路上也有很多資訊喔～祝福你抽到最適合你的宿舍！🥺🥺")]
    elif input == "讓我看看最豪華的選項吧！":
        return [TextSendMessage(text="看來最適合你的是【敬一】"),
                ImageSendMessage(original_content_url='https://i.imgur.com/MnNbE2j.jpeg',
                                 preview_image_url='https://i.imgur.com/MnNbE2j.jpeg'),
                TextSendMessage(text="除了這邊的懶人包以外網路上也有很多資訊喔～祝福你抽到最適合你的宿舍！🥺🥺")]


def get_dorm_result_woman(input):
    if input == "想要雙人房":
        return [TextSendMessage(text="看來最適合你的是【勝三】"),
                ImageSendMessage(original_content_url='https://i.imgur.com/REqSJgT.jpeg',
                                 preview_image_url='https://i.imgur.com/REqSJgT.jpeg'),
                TextSendMessage(text="除了這邊的懶人包以外網路上也有很多資訊喔～祝福你抽到最適合你的宿舍！🥺🥺")]
    elif input == "給我套房！":
        return [TextSendMessage(text="看來最適合你的是【勝八】"),
                ImageSendMessage(original_content_url='https://i.imgur.com/E0Cz8Up.jpeg',
                                 preview_image_url='https://i.imgur.com/E0Cz8Up.jpeg'),
                TextSendMessage(text="除了這邊的懶人包以外網路上也有很多資訊喔～祝福你抽到最適合你的宿舍！🥺🥺")]
    elif input == "我愛三人房":
        return [TextSendMessage(text="看來最適合你的是【勝二】"),
                ImageSendMessage(original_content_url='https://i.imgur.com/lhvI1f8.jpeg',
                                 preview_image_url='https://i.imgur.com/lhvI1f8.jpeg'),
                TextSendMessage(text="除了這邊的懶人包以外網路上也有很多資訊喔～祝福你抽到最適合你的宿舍！🥺🥺")]
    elif input == "木製傢俱我的愛":
        return [TextSendMessage(text="看來最適合你的是【勝九】"),
                ImageSendMessage(original_content_url='https://i.imgur.com/UqvVmhm.jpeg',
                                 preview_image_url='https://i.imgur.com/UqvVmhm.jpeg'),
                TextSendMessage(text="除了這邊的懶人包以外網路上也有很多資訊喔～祝福你抽到最適合你的宿舍！🥺🥺")]


def text_reply(toReply):
    return TextSendMessage(text=toReply)


def line_emoji_x1(index, productID_string, emojiId_string):
    return {
        "index": index,
        "productId": productID_string,
        "emojiId": emojiId_string
    }
