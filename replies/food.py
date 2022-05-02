from linebot.models import *

food_dict = {
    "找吃的！",
    "早餐！",
    "午餐！",
    "晚餐！",
    "宵夜！"
}


def reply(input,username):
    if input == "找吃的！":
        return find_eat()
    elif input == "早餐！":
        return return_meal("breakfast")
    elif input == "午餐！":
        return return_meal("lunch")
    elif input == "晚餐！":
        return return_meal("dinner")
    elif input == "宵夜！":
        return return_meal("night_supper")


def find_eat():
    return TextSendMessage(
        text="想吃哪一餐？",
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(action=MessageAction(label="早餐", text="早餐！")),
                QuickReplyButton(action=MessageAction(label="午餐", text="午餐！")),
                QuickReplyButton(action=MessageAction(label="晚餐", text="晚餐！")),
                QuickReplyButton(action=MessageAction(label="宵夜", text="宵夜！"))
            ])
    )

def return_meal(meal):
    if meal == "breakfast":
        return TextSendMessage("[早餐地圖]")
    elif meal == "lunch":
        return TextSendMessage("[午餐地圖]")
    elif meal == "dinner":
        return TextSendMessage("[晚餐地圖]")
    elif meal == "night_supper":
        return TextSendMessage("[宵夜地圖]")
