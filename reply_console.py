from replies import dorm, food
from linebot.models import(
    TextSendMessage
)

def reply(input,username):
    if input in dorm.dorm_dict:
        return dorm.reply(input,username)
    elif input in food.food_dict:
        return food.reply(input,username)
    return TextSendMessage(text="[ 這邊還沒做好 ]")