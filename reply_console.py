from replies import dorm, food
from linebot.models import(
    TextSendMessage
)

def reply(input):
    if input in dorm.dorm_dict:
        return dorm.reply(input)
    elif input in food.food_dict:
        return food.reply(input)
    return TextSendMessage(text="[ 這邊還沒做好 ]")