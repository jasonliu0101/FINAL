from linebot.models import *
dict = {
    "我要加社團！"
}

def reply(input):
    if input == "我要加社團！":
        return[TextSendMessage(text="這裡是成大人必加的臉書社團，快加入吧！😍😍"),
               TextSendMessage(text="▪成大二手交流版 \n https://www.facebook.com/groups/384397068383429 \n ▪成大選課 \n https://www.facebook.com/groups/637099219647956/ \n ▪NCKU HUB(選課心得分享）\n https://nckuhub.com\n ▪成大租屋 \n https://www.facebook.com/groups/NCKUhouse/ \n ▪成大講座 \n https://www.facebook.com/groups/762866160499626/" )]
    else:
        return "NOT_THIS"

