from linebot.models import *

def reply(input):
    if input == "我要加社團！":
        return[TextSendMessage(text="這裡是成大人必加的臉書社團，快加入吧！😍😍"),
               TextSendMessage(text="成大二手交流版 https://www.facebook.com/groups/384397068383429 \n 成大選課 https://www.facebook.com/groups/637099219647956/ \n NCKU HUB(選課心得分享）https://nckuhub.com\n 成大租屋 https://www.facebook.com/groups/NCKUhouse/ \n 成大講座https://www.facebook.com/groups/762866160499626/" )]

