from linebot.models import *

class_dict = {
    "我要選課！",
    "選課查詢",
    "單科加選",
    "棄選流程",
    "通識登記一",
    "通識登記二"
}


def reply(input):
    if input == "我要選課！":
        return testFMS()

def testFMS():
    return [FlexSendMessage(
        alt_text='Flex Message',
        contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://imgur.com/e8zohEF.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "NCKU 選課導覽",
        "weight": "bold",
        "size": "xxl",
        "color": "#66DD00"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "選課查詢",
          "uri": "https://i.imgur.com/Y3DKI9C.jpeg"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "單科加選",
          "uri": "https://i.imgur.com/rsB1MEZ.jpeg"
        },
        "margin": "md",
        "offsetBottom": "none",
        "offsetStart": "none",
        "offsetEnd": "none",
        "offsetTop": "none"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "棄選流程",
          "uri": "https://i.imgur.com/P9PES7z.jpeg'"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "通識登記一",
          "uri": "https://i.imgur.com/gUttt07.jpeg"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "通識登記二",
          "uri": "https://i.imgur.com/AEnaRAZ.jpeg"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "http://linecorp.com/"
        }
      }
    ],
    "flex": 0
  }
}
        
    )]
