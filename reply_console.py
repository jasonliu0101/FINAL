from replies import dorm, food, fb, classes
from linebot.models import(
    TextSendMessage
)

def reply(input,username):  #處理main傳入的資訊，逐個比對關鍵字是否有出現對應的回應
    if input in dorm.dorm_dict:
        return dorm.reply(input,username)
    elif input in food.food_dict:
        return food.reply(input,username)
    elif input in fb.dict:
        return fb.reply(input)
    elif input in classes.dict:  #class is a reserved word so name changed
        return classes.reply(input)
    return TextSendMessage(text="[ 這邊還沒做好 ]")
