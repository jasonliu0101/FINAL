from replies import dorm, food, fb, classes, road
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
    elif input in classes.class_dict:  #class is a reserved word so name changed
        return classes.reply(input)
    elif input in road.road_dict:
        return road.reply(input)
    elif input == "alarm":
        return TextSendMessage(text="https://liff.line.me/1645278921-kWRPP32q/?accountId=850gmohw")
    return TextSendMessage(text="要用選單輸入哦！")
