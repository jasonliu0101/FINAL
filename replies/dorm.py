from linebot.models import *

dorm_dict = {
    "找宿舍！",
    "我是男生！",
    "我是女生！",
    "TypeA",
    "TypeB",
    "TypeC",
    "TypeD"
}


def reply(input):
    if input == "找宿舍！":
        return choose_sex()

    elif input == "我是男生！":
        return choose_dorm("man")

    elif input == "我是女生！":
        return choose_dorm("woman")

    elif input == "TypeA":
        return get_dorm_result_woman(input)

    elif input == "TypeB":
        return get_dorm_result_woman(input)

    elif input == "TypeC":
        return get_dorm_result_woman(input)

    elif input == "TypeD":
        return get_dorm_result_woman(input)



def choose_sex():
    return [TextSendMessage(
        text="請問您的性別！",
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(action=MessageAction(label="男生", text="我是男生！")),
                QuickReplyButton(action=MessageAction(label="女生", text="我是女生！"))
            ])
    )]

def choose_dorm(sex):
    if sex == "man":
        return [ImageSendMessage(original_content_url='https://i.imgur.com/JXTwuZw.jpeg',preview_image_url='https://i.imgur.com/JXTwuZw.jpeg'),
            TextSendMessage(
            text="請問您想要哪一種宿舍！",
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(action=MessageAction(label="TypeA", text="TypeA")),
                    QuickReplyButton(action=MessageAction(label="TypeB", text="TypeB")),
                    QuickReplyButton(action=MessageAction(label="TypeC", text="TypeC")),
                    QuickReplyButton(action=MessageAction(label="TypeD", text="TypeD"))
                ])
        )]
    elif sex == "woman":
        return [ImageSendMessage(original_content_url='https://i.imgur.com/llOZodk.jpeg',preview_image_url='https://i.imgur.com/llOZodk.jpeg'),
            TextSendMessage(
            text="請問您想要哪一種宿舍！",
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(action=MessageAction(label="TypeA", text="TypeA")),
                    QuickReplyButton(action=MessageAction(label="TypeB", text="TypeB")),
                    QuickReplyButton(action=MessageAction(label="TypeC", text="TypeC")),
                    QuickReplyButton(action=MessageAction(label="TypeD", text="TypeD"))
                ])
        )]


def get_dorm_result_man(input):
    if input == "TypeA":
        return [TextSendMessage(text="看來最適合你的是【勝一】"),ImageSendMessage(original_content_url='https://i.imgur.com/X6fPDEi.jpeg',preview_image_url='https://i.imgur.com/X6fPDEi.jpeg')]
    elif input == "TypeB":
        return [TextSendMessage(text="看來最適合你的是【光一】"),ImageSendMessage(original_content_url='https://i.imgur.com/ztLc7oS.jpeg',preview_image_url='https://i.imgur.com/ztLc7oS.jpeg')]
    elif input == "TypeC":
        return [TextSendMessage(text="看來最適合你的是【光二】"),ImageSendMessage(original_content_url='https://i.imgur.com/lu1ckVy.jpeg',preview_image_url='https://i.imgur.com/lu1ckVy.jpeg')]
    elif input == "TypeD":
        return [TextSendMessage(text="看來最適合你的是【敬一】"),ImageSendMessage(original_content_url='https://i.imgur.com/MnNbE2j.jpeg',preview_image_url='https://i.imgur.com/MnNbE2j.jpeg')]

def get_dorm_result_woman(input):
    if input == "TypeA":
        return [TextSendMessage(text="看來最適合你的是【勝三】"),ImageSendMessage(original_content_url='https://i.imgur.com/REqSJgT.jpeg',preview_image_url='https://i.imgur.com/REqSJgT.jpeg')]
    elif input == "TypeB":
        return [TextSendMessage(text="看來最適合你的是【勝八】"),ImageSendMessage(original_content_url='https://i.imgur.com/E0Cz8Up.jpeg',preview_image_url='https://i.imgur.com/E0Cz8Up.jpeg')]
    elif input == "TypeC":
        return [TextSendMessage(text="看來最適合你的是【勝二】"),ImageSendMessage(original_content_url='https://i.imgur.com/lhvI1f8.jpeg',preview_image_url='https://i.imgur.com/lhvI1f8.jpeg')]
    elif input == "TypeD":
        return [TextSendMessage(text="看來最適合你的是【勝九】"),ImageSendMessage(original_content_url='https://i.imgur.com/UqvVmhm.jpeg',preview_image_url='https://i.imgur.com/UqvVmhm.jpeg')]

def text_reply(toReply):
    return TextSendMessage(text=toReply)

