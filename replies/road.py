from linebot.models import * 

road_dict = {
    "成大人之道6選2",
    "踏溯台南!",
    "小路線2選1",
    "大路線2選1",
    "水乳交融",
    "走尋老月津",
    "要搭公車喔!流瀾小西腳",
    "騎腳踏車就Ok光點西竹圍",
    "環境",
    "文化",
    "人文路線",
    "流瀾小西腳集合地點",
    "光點西竹圍集合地點",
    "大路線集合地點",
    "成功湖側",
    "[成功校區]博物館",
    "大成館正門口",
    "歷史系館正門口",
    "科教中心正門口"
}

def reply(input):
    if input =="成大人之道6選2":
        return school()

    elif input =="踏溯台南!":
        return testFMS()

    elif input =="小路線2選1":
        return testnear()

    elif input =="大路線2選1":
        return testfar()

    elif input =="水乳交融":
        return far1()

    elif input =="走尋老月津":
        return far2()

    elif input == "要搭公車喔!流瀾小西腳":
        return near1()

    elif input == "騎腳踏車就Ok光點西竹圍":
        return near2()

    elif input == "環境":
        return school2()

    elif input == "文化":
        return school1()

    elif input == "人文路線":
        return schoolc()

    elif input == "流瀾小西腳集合地點":
        return LocationSendMessage(
            title='流瀾小西腳集合地點',                   
            address='成功大學光復校區中文系館前石桌',               
            latitude=23.000359860755243,
            longitude=120.21789006828647
        )
    elif input == "光點西竹圍集合地點":
        return LocationSendMessage(
            title='光點西竹圍集合地點',                   
            address='成功大學光復校區光口警衛室後、中正堂側廣場',               
            latitude=22.996592124816676,
            longitude=120.21667107940547
        )
    elif input == "大路線集合地點":
        return LocationSendMessage(
            title='大路線集合地點',                   
            address='成功大學光復校區修齊大樓前',               
            latitude=23.00081250635751,
            longitude=120.21783190047728
        )
    elif input == "成功湖側":
        return LocationSendMessage(
            title='成大人之道小西門起路線',                   
            address='成功大學光復校區成功湖側',               
            latitude=23.000317696090534,
            longitude=120.2172642389391
        )
    elif input == "[成功校區]博物館":
        return LocationSendMessage(
            title='成大人之道博物館起路線',                   
            address='成功大學成功校區博物館前',               
            latitude=22.99682020299907,
            longitude=120.21958376227306
        )
    elif input == "大成館正門口":
        return LocationSendMessage(
            title='成大人之道榕園路線',                   
            address='成功大學大成館正門口',               
            latitude=22.999692262660368,
            longitude=120.21597163191801
        )
    elif input == "歷史系館正門口":
        return LocationSendMessage(
            title='成大人之道岩石路線',                   
            address='成功大學歷史系館正門口',               
            latitude=22.999571090506745,
            longitude=120.2173025894045
        )
    elif input == "科教中心正門口":
        return LocationSendMessage(
            title='成大人之道科學路線',                   
            address='成功大學歷史系館正門口',               
            latitude=22.997903,
            longitude=120.218641
        )   

def testFMS():
 return [FlexSendMessage(
    alt_text='Flex Message',
    contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scontent-tpe1-1.xx.fbcdn.net/v/t1.18169-9/22405638_348875472224073_7317239583593503794_n.png?_nc_cat=103&ccb=1-6&_nc_sid=09cbfe&_nc_ohc=5hzAdxI8LTsAX8tW_3v&_nc_ht=scontent-tpe1-1.xx&oh=00_AT_HIXI5xKOdcMtTGsWS4zYpx5b3QIpRIqY3fSQVVghrvg&oe=629C29E9",
    "size": "full",
    "aspectRatio": "20:20",
    "aspectMode": "fit",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    },
    "animated": True
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "踏溯台南規則",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": "https://cdn-icons-png.flaticon.com/512/1040/1040446.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://cdn-icons-png.flaticon.com/512/1040/1040446.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://cdn-icons-png.flaticon.com/512/1040/1040446.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://cdn-icons-png.flaticon.com/512/1040/1040446.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://cdn-icons-png.flaticon.com/512/395/395841.png"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Place",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "台南府城Tainan",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Time",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "110學年度下學期",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "box",
        "layout": "baseline",
        "contents": [],
        "margin": "sm"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "md",
        "action": {
          "type": "uri",
          "label": "講座課",
          "uri": "http://exptainan.liberal.ncku.edu.tw/index.php?lang=cht&task=home"
        },
        "color": "#973635"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "md",
        "action": {
          "type": "message",
          "label": "成大人之道",
          "text": "成大人之道6選2"
        },
        "color": "#973635"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "md",
        "action": {
          "type": "message",
          "label": "大路線",
          "text": "大路線2選1"
        },
        "color": "#6ebbbd"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "md",
        "action": {
          "type": "message",
          "label": "小路線",
          "text": "小路線2選1"
        },
        "color": "#c65e4b"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "md",
        "action": {
          "type": "message",
          "label": "其他Q&A",
          "text": "QA"
        },
        "color": "#b8abbd"
      },{
        "type": "button",
        "style": "primary",
        "height": "md",
        "action": {
          "type":  "uri",
          "label": "課室地圖",
          "uri": "http://exptainan.liberal.ncku.edu.tw/index.php?option=module&lang=cht&task=pageinfo&id=946&index=4"
        },
        "color": "#94abc3"
      }
    ],
    "flex": 0
  },
  "styles": {
    "footer": {
      "separator": True,
      "separatorColor": "#973635"
    }
  }
}
    )]

def school():
    return TextSendMessage(
    text='請選擇',
    quick_reply=QuickReply(
    items=[
        QuickReplyButton(action=MessageAction(label='文化', text='文化')),
        QuickReplyButton(action=MessageAction(label='環境', text='環境')),
    ]))
    
def school1():
    return [FlexSendMessage(
    alt_text='Flex Message',
    contents=
    {"type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://img.ltn.com.tw/Upload/news/600/2020/04/15/phpjCytpt.jpg",
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
          "text": "成大人之道",
          "weight": "bold",
          "size": "xl"
        },
        {
          "type": "box",
          "layout": "baseline",
          "margin": "md",
          "contents": [
            {
              "type": "icon",
              "size": "sm",
              "url": "https://web.ncku.edu.tw/var/file/0/1000/img/1215/ncku-logo2.jpg"
            },
            {
              "type": "icon",
              "size": "sm",
              "url": "https://web.ncku.edu.tw/var/file/0/1000/img/1215/ncku-logo1.jpg"
            },
            {
              "type": "text",
              "text": "人文",
              "color": "#323933"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "margin": "lg",
          "spacing": "sm",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "Place",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 1
                },
                {
                  "type": "text",
                  "text": "701台南市東區大學路1號",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "Time",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 1
                },
                {
                  "type": "text",
                  "text": "半日遊",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            }
          ]
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
          "style": "primary",
          "height": "sm",
          "action": {
            "type": "uri",
            "label": "路線介紹",
            "uri": "http://exptainan.liberal.ncku.edu.tw/index.php?option=module&lang=cht&task=showlist&id=700&index=1"
          },
          "color": "#52bb7d"
        },
        {
          "type": "button",
          "style": "primary",
          "height": "sm",
          "action": {
            "type": "message",
            "label": "路線選擇",
            "text": "人文路線"
          },
          "color": "#52bb7d"
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [],
          "margin": "sm"
        }
      ],
      "flex": 0
    }}
    )]
    
def school2():
  return [FlexSendMessage(
    alt_text='Flex Message',
    contents=
    {
    "type": "carousel",
    "contents": [
      {
        "type": "bubble",
        "size": "mega",
        "header": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "FROM",
                  "color": "#ffffff66",
                  "size": "sm"
                },
                {
                  "type": "text",
                  "text": "校園植物(起)",
                  "color": "#ffffff",
                  "size": "xl",
                  "flex": 4,
                  "weight": "bold"
                }
              ]
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "TO",
                  "color": "#ffffff66",
                  "size": "sm"
                },
                {
                  "type": "text",
                  "text": "石在有趣(終)",
                  "color": "#ffffff",
                  "size": "xl",
                  "flex": 4,
                  "weight": "bold"
                }
              ]
            }
          ],
          "paddingAll": "20px",
          "backgroundColor": "#52bb7d",
          "spacing": "md",
          "height": "154px",
          "paddingTop": "22px"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "Total: 2 hour",
              "color": "#b7b7b7",
              "size": "xs"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "起點",
                  "size": "sm",
                  "margin": "none",
                  "position": "relative",
                  "wrap": True
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "filler"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [],
                      "cornerRadius": "30px",
                      "height": "12px",
                      "width": "12px",
                      "borderColor": "#EF454D",
                      "borderWidth": "2px"
                    },
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 0
                },
                {
                  "type": "text",
                  "text": "榕園",
                  "gravity": "center",
                  "flex": 4,
                  "size": "sm"
                }
              ],
              "spacing": "lg",
              "cornerRadius": "30px",
              "margin": "xl"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 1
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "filler"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [],
                          "width": "2px",
                          "backgroundColor": "#B7B7B7"
                        },
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 1
                    }
                  ],
                  "width": "12px"
                },
                {
                  "type": "text",
                  "text": "Walk",
                  "gravity": "center",
                  "flex": 4,
                  "size": "xs",
                  "color": "#8c8c8c"
                }
              ],
              "spacing": "lg",
              "height": "64px"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [],
                  "flex": 1
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "filler"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [],
                      "cornerRadius": "30px",
                      "width": "12px",
                      "height": "12px",
                      "borderWidth": "2px",
                      "borderColor": "#6486E3"
                    },
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 0
                },
                {
                  "type": "text",
                  "text": "光復校區",
                  "gravity": "center",
                  "flex": 4,
                  "size": "sm"
                }
              ],
              "spacing": "lg",
              "cornerRadius": "30px"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 1
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "filler"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [],
                          "width": "2px",
                          "backgroundColor": "#6486E3"
                        },
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 1
                    }
                  ],
                  "width": "12px"
                },
                {
                  "type": "text",
                  "text": "Walk",
                  "gravity": "center",
                  "flex": 4,
                  "size": "xs",
                  "color": "#8c8c8c"
                }
              ],
              "spacing": "lg",
              "height": "64px"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "終點",
                  "gravity": "center",
                  "size": "sm"
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "filler"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [],
                      "cornerRadius": "30px",
                      "width": "12px",
                      "height": "12px",
                      "borderColor": "#6486E3",
                      "borderWidth": "2px"
                    },
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 0
                },
                {
                  "type": "text",
                  "text": "歷史系館正門口",
                  "gravity": "center",
                  "flex": 4,
                  "size": "sm"
                }
              ],
              "spacing": "lg",
              "cornerRadius": "30px"
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
              "style": "primary",
              "height": "sm",
              "action": {
                "type": "message",
                "label": "集合地點",
                "text": "大成館正門口"
              },
              "color": "#bc9555"
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [],
              "margin": "sm"
            }
          ],
          "flex": 0
        }
      },
      {
        "type": "bubble",
        "size": "mega",
        "header": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "FROM",
                  "color": "#ffffff66",
                  "size": "sm"
                },
                {
                  "type": "text",
                  "text": "石在有趣(起)",
                  "color": "#ffffff",
                  "size": "xl",
                  "flex": 4,
                  "weight": "bold"
                }
              ]
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "TO",
                  "color": "#ffffff66",
                  "size": "sm"
                },
                {
                  "type": "text",
                  "text": "校園植物(終)",
                  "color": "#ffffff",
                  "size": "xl",
                  "flex": 4,
                  "weight": "bold"
                }
              ]
            }
          ],
          "paddingAll": "20px",
          "backgroundColor": "#52bb7d",
          "spacing": "md",
          "height": "154px",
          "paddingTop": "22px"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "Total: 2 hour",
              "color": "#b7b7b7",
              "size": "xs"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "起點",
                  "size": "sm",
                  "margin": "none",
                  "position": "relative",
                  "wrap": True
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "filler"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [],
                      "cornerRadius": "30px",
                      "height": "12px",
                      "width": "12px",
                      "borderColor": "#EF454D",
                      "borderWidth": "2px"
                    },
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 0
                },
                {
                  "type": "text",
                  "text": "歷史系館正門口",
                  "gravity": "center",
                  "flex": 4,
                  "size": "sm"
                }
              ],
              "spacing": "lg",
              "cornerRadius": "30px",
              "margin": "xl"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 1
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "filler"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [],
                          "width": "2px",
                          "backgroundColor": "#B7B7B7"
                        },
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 1
                    }
                  ],
                  "width": "12px"
                },
                {
                  "type": "text",
                  "text": "Walk",
                  "gravity": "center",
                  "flex": 4,
                  "size": "xs",
                  "color": "#8c8c8c"
                }
              ],
              "spacing": "lg",
              "height": "64px"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [],
                  "flex": 1
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "filler"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [],
                      "cornerRadius": "30px",
                      "width": "12px",
                      "height": "12px",
                      "borderWidth": "2px",
                      "borderColor": "#6486E3"
                    },
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 0
                },
                {
                  "type": "text",
                  "text": "光復校區",
                  "gravity": "center",
                  "flex": 4,
                  "size": "sm"
                }
              ],
              "spacing": "lg",
              "cornerRadius": "30px"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 1
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "filler"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [],
                          "width": "2px",
                          "backgroundColor": "#6486E3"
                        },
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 1
                    }
                  ],
                  "width": "12px"
                },
                {
                  "type": "text",
                  "text": "Walk",
                  "gravity": "center",
                  "flex": 4,
                  "size": "xs",
                  "color": "#8c8c8c"
                }
              ],
              "spacing": "lg",
              "height": "64px"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "終點",
                  "gravity": "center",
                  "size": "sm"
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "filler"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [],
                      "cornerRadius": "30px",
                      "width": "12px",
                      "height": "12px",
                      "borderColor": "#6486E3",
                      "borderWidth": "2px"
                    },
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 0
                },
                {
                  "type": "text",
                  "text": "榕園",
                  "gravity": "center",
                  "flex": 4,
                  "size": "sm"
                }
              ],
              "spacing": "lg",
              "cornerRadius": "30px"
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
              "style": "primary",
              "height": "sm",
              "action": {
                "type": "message",
                "label": "集合地點",
                "text": "歷史系館正門口"
              },
              "color": "#bc9555"
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [],
              "margin": "sm"
            }
          ],
          "flex": 0
        }
      },
      {
        "type": "bubble",
        "size": "mega",
        "header": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "FROM",
                  "color": "#ffffff66",
                  "size": "sm"
                },
                {
                  "type": "text",
                  "text": "校園植物(起)",
                  "color": "#ffffff",
                  "size": "xl",
                  "flex": 4,
                  "weight": "bold"
                }
              ]
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "TO",
                  "color": "#ffffff66",
                  "size": "sm"
                },
                {
                  "type": "text",
                  "text": "來玩科學(終)",
                  "color": "#ffffff",
                  "size": "xl",
                  "flex": 4,
                  "weight": "bold"
                }
              ]
            }
          ],
          "paddingAll": "20px",
          "backgroundColor": "#52bb7d",
          "spacing": "md",
          "height": "154px",
          "paddingTop": "22px"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "Total: 2 hour",
              "color": "#b7b7b7",
              "size": "xs"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "起點",
                  "size": "sm",
                  "margin": "none",
                  "position": "relative",
                  "wrap": True
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "filler"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [],
                      "cornerRadius": "30px",
                      "height": "12px",
                      "width": "12px",
                      "borderColor": "#EF454D",
                      "borderWidth": "2px"
                    },
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 0
                },
                {
                  "type": "text",
                  "text": "榕園",
                  "gravity": "center",
                  "flex": 4,
                  "size": "sm"
                }
              ],
              "spacing": "lg",
              "cornerRadius": "30px",
              "margin": "xl"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 1
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "filler"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [],
                          "width": "2px",
                          "backgroundColor": "#B7B7B7"
                        },
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 1
                    }
                  ],
                  "width": "12px"
                },
                {
                  "type": "text",
                  "text": "Walk",
                  "gravity": "center",
                  "flex": 4,
                  "size": "xs",
                  "color": "#8c8c8c"
                }
              ],
              "spacing": "lg",
              "height": "64px"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [],
                  "flex": 1
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "filler"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [],
                      "cornerRadius": "30px",
                      "width": "12px",
                      "height": "12px",
                      "borderWidth": "2px",
                      "borderColor": "#6486E3"
                    },
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 0
                },
                {
                  "type": "text",
                  "text": "光復校區",
                  "gravity": "center",
                  "flex": 4,
                  "size": "sm"
                }
              ],
              "spacing": "lg",
              "cornerRadius": "30px"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 1
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "filler"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [],
                          "width": "2px",
                          "backgroundColor": "#6486E3"
                        },
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 1
                    }
                  ],
                  "width": "12px"
                },
                {
                  "type": "text",
                  "text": "Walk",
                  "gravity": "center",
                  "flex": 4,
                  "size": "xs",
                  "color": "#8c8c8c"
                }
              ],
              "spacing": "lg",
              "height": "64px"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "終點",
                  "gravity": "center",
                  "size": "sm"
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "filler"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [],
                      "cornerRadius": "30px",
                      "width": "12px",
                      "height": "12px",
                      "borderColor": "#6486E3",
                      "borderWidth": "2px"
                    },
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 0
                },
                {
                  "type": "text",
                  "text": "理學院科學教育中心",
                  "gravity": "center",
                  "flex": 4,
                  "size": "sm"
                }
              ],
              "spacing": "lg",
              "cornerRadius": "30px"
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
              "style": "primary",
              "height": "sm",
              "action": {
                "type": "message",
                "label": "集合地點",
                "text": "大成館正門口"
              },
              "color": "#bc9555"
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [],
              "margin": "sm"
            }
          ],
          "flex": 0
        }
      },
      {
        "type": "bubble",
        "size": "mega",
        "header": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "FROM",
                  "color": "#ffffff66",
                  "size": "sm"
                },
                {
                  "type": "text",
                  "text": "來玩科學(起)",
                  "color": "#ffffff",
                  "size": "xl",
                  "flex": 4,
                  "weight": "bold"
                }
              ]
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "TO",
                  "color": "#ffffff66",
                  "size": "sm"
                },
                {
                  "type": "text",
                  "text": "校園植物(終)",
                  "color": "#ffffff",
                  "size": "xl",
                  "flex": 4,
                  "weight": "bold"
                }
              ]
            }
          ],
          "paddingAll": "20px",
          "backgroundColor": "#52bb7d",
          "spacing": "md",
          "height": "154px",
          "paddingTop": "22px"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "Total: 2 hour",
              "color": "#b7b7b7",
              "size": "xs"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "起點",
                  "size": "sm",
                  "margin": "none",
                  "position": "relative",
                  "wrap": True
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "filler"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [],
                      "cornerRadius": "30px",
                      "height": "12px",
                      "width": "12px",
                      "borderColor": "#EF454D",
                      "borderWidth": "2px"
                    },
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 0
                },
                {
                  "type": "text",
                  "text": "理學院科教中心",
                  "gravity": "center",
                  "flex": 4,
                  "size": "sm"
                }
              ],
              "spacing": "lg",
              "cornerRadius": "30px",
              "margin": "xl"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 1
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "filler"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [],
                          "width": "2px",
                          "backgroundColor": "#B7B7B7"
                        },
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 1
                    }
                  ],
                  "width": "12px"
                },
                {
                  "type": "text",
                  "text": "Walk",
                  "gravity": "center",
                  "flex": 4,
                  "size": "xs",
                  "color": "#8c8c8c"
                }
              ],
              "spacing": "lg",
              "height": "64px"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [],
                  "flex": 1
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "filler"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [],
                      "cornerRadius": "30px",
                      "width": "12px",
                      "height": "12px",
                      "borderWidth": "2px",
                      "borderColor": "#6486E3"
                    },
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 0
                },
                {
                  "type": "text",
                  "text": "成功校區",
                  "gravity": "center",
                  "flex": 4,
                  "size": "sm"
                }
              ],
              "spacing": "lg",
              "cornerRadius": "30px"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 1
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "filler"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [],
                          "width": "2px",
                          "backgroundColor": "#6486E3"
                        },
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 1
                    }
                  ],
                  "width": "12px"
                },
                {
                  "type": "text",
                  "text": "Walk",
                  "gravity": "center",
                  "flex": 4,
                  "size": "xs",
                  "color": "#8c8c8c"
                }
              ],
              "spacing": "lg",
              "height": "64px"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "終點",
                  "gravity": "center",
                  "size": "sm"
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "filler"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [],
                      "cornerRadius": "30px",
                      "width": "12px",
                      "height": "12px",
                      "borderColor": "#6486E3",
                      "borderWidth": "2px"
                    },
                    {
                      "type": "filler"
                    }
                  ],
                  "flex": 0
                },
                {
                  "type": "text",
                  "text": "理學院科學教育中心",
                  "gravity": "center",
                  "flex": 4,
                  "size": "sm"
                }
              ],
              "spacing": "lg",
              "cornerRadius": "30px"
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
              "style": "primary",
              "height": "sm",
              "action": {
                "type": "message",
                "label": "集合地點",
                "text": "科教中心正門口"
              },
              "color": "#bc9555"
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [],
              "margin": "sm"
            }
          ],"flex": 0
        }
      }
    ]
  }
  )]
  
def schoolc():
    return [FlexSendMessage(
    alt_text='Flex Message',
    contents=
    {
    "type": "carousel",
    "contents": [
        {
            "type": "bubble",
            "size": "mega",
            "header": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "FROM",
                      "color": "#ffffff66",
                      "size": "sm"
                    },
                    {
                      "type": "text",
                      "text": "博物館區(起)",
                      "color": "#ffffff",
                      "size": "xl",
                      "flex": 4,
                      "weight": "bold"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "TO",
                      "color": "#ffffff66",
                      "size": "sm"
                    },
                    {
                      "type": "text",
                      "text": "小西門區+(終)",
                      "color": "#ffffff",
                      "size": "xl",
                      "flex": 4,
                      "weight": "bold"
                    }
                  ]
                }
              ],
              "paddingAll": "20px",
              "backgroundColor": "#bc9555",
              "spacing": "md",
              "height": "154px",
              "paddingTop": "22px"
            },
            "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "Total: 2 hour",
                  "color": "#b7b7b7",
                  "size": "xs"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "起點",
                      "size": "sm",
                      "margin": "none",
                      "position": "relative",
                      "wrap": True
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "filler"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [],
                          "cornerRadius": "30px",
                          "height": "12px",
                          "width": "12px",
                          "borderColor": "#EF454D",
                          "borderWidth": "2px"
                        },
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 0
                    },
                    {
                      "type": "text",
                      "text": "[成功校區] 成大博物館前",
                      "gravity": "center",
                      "flex": 4,
                      "size": "sm"
                    }
                  ],
                  "spacing": "lg",
                  "cornerRadius": "30px",
                  "margin": "xl"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 1
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "box",
                          "layout": "horizontal",
                          "contents": [
                            {
                              "type": "filler"
                            },
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [],
                              "width": "2px",
                              "backgroundColor": "#B7B7B7"
                            },
                            {
                              "type": "filler"
                            }
                          ],
                          "flex": 1
                        }
                      ],
                      "width": "12px"
                    },
                    {
                      "type": "text",
                      "text": "Walk",
                      "gravity": "center",
                      "flex": 4,
                      "size": "xs",
                      "color": "#8c8c8c"
                    }
                  ],
                  "spacing": "lg",
                  "height": "64px"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [],
                      "flex": 1
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "filler"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [],
                          "cornerRadius": "30px",
                          "width": "12px",
                          "height": "12px",
                          "borderWidth": "2px",
                          "borderColor": "#6486E3"
                        },
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 0
                    },
                    {
                      "type": "text",
                      "text": "光復校區",
                      "gravity": "center",
                      "flex": 4,
                      "size": "sm"
                    }
                  ],
                  "spacing": "lg",
                  "cornerRadius": "30px"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 1
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "box",
                          "layout": "horizontal",
                          "contents": [
                            {
                              "type": "filler"
                            },
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [],
                              "width": "2px",
                              "backgroundColor": "#6486E3"
                            },
                            {
                              "type": "filler"
                            }
                          ],
                          "flex": 1
                        }
                      ],
                      "width": "12px"
                    },
                    {
                      "type": "text",
                      "text": "Walk",
                      "gravity": "center",
                      "flex": 4,
                      "size": "xs",
                      "color": "#8c8c8c"
                    }
                  ],
                  "spacing": "lg",
                  "height": "64px"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "終點",
                      "gravity": "center",
                      "size": "sm"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "filler"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [],
                          "cornerRadius": "30px",
                          "width": "12px",
                          "height": "12px",
                          "borderColor": "#6486E3",
                          "borderWidth": "2px"
                        },
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 0
                    },
                    {
                      "type": "text",
                      "text": "[光復校區]小西門",
                      "gravity": "center",
                      "flex": 4,
                      "size": "sm"
                    }
                  ],
                  "spacing": "lg",
                  "cornerRadius": "30px"
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
                  "style": "primary",
                  "height": "sm",
                  "action": {
                    "type": "message",
                    "label": "集合地點",
                    "text": "[成功校區]博物館"
                  },
                  "color": "#52bb7d"
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [],
                  "margin": "sm"
                }
              ],
              "flex": 0
            }
        },
        {
            "type": "bubble",
            "size": "mega",
            "header": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "FROM",
                      "color": "#ffffff66",
                      "size": "sm"
                    },
                    {
                      "type": "text",
                      "text": "小西門區(起)",
                      "color": "#ffffff",
                      "size": "xl",
                      "flex": 4,
                      "weight": "bold"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "TO",
                      "color": "#ffffff66",
                      "size": "sm"
                    },
                    {
                      "type": "text",
                      "text": "博物館區(終)",
                      "color": "#ffffff",
                      "size": "xl",
                      "flex": 4,
                      "weight": "bold"
                    }
                  ]
                }
              ],
              "paddingAll": "20px",
              "backgroundColor": "#bc9555",
              "spacing": "md",
              "height": "154px",
              "paddingTop": "22px"
            },
            "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "Total: 2 hour",
                  "color": "#b7b7b7",
                  "size": "xs"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "起點",
                      "size": "sm",
                      "margin": "none",
                      "position": "relative",
                      "wrap": True
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "filler"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [],
                          "cornerRadius": "30px",
                          "height": "12px",
                          "width": "12px",
                          "borderColor": "#EF454D",
                          "borderWidth": "2px"
                        },
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 0
                    },
                    {
                      "type": "text",
                      "text": "[光復校區] 小西門",
                      "gravity": "center",
                      "flex": 4,
                      "size": "sm"
                    }
                  ],
                  "spacing": "lg",
                  "cornerRadius": "30px",
                  "margin": "xl"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 1
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "box",
                          "layout": "horizontal",
                          "contents": [
                            {
                              "type": "filler"
                            },
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [],
                              "width": "2px",
                              "backgroundColor": "#B7B7B7"
                            },
                            {
                              "type": "filler"
                            }
                          ],
                          "flex": 1
                        }
                      ],
                      "width": "12px"
                    },
                    {
                      "type": "text",
                      "text": "Walk",
                      "gravity": "center",
                      "flex": 4,
                      "size": "xs",
                      "color": "#8c8c8c"
                    }
                  ],
                  "spacing": "lg",
                  "height": "64px"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [],
                      "flex": 1
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "filler"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [],
                          "cornerRadius": "30px",
                          "width": "12px",
                          "height": "12px",
                          "borderWidth": "2px",
                          "borderColor": "#6486E3"
                        },
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 0
                    },
                    {
                      "type": "text",
                      "text": "成功校區",
                      "gravity": "center",
                      "flex": 4,
                      "size": "sm"
                    }
                  ],
                  "spacing": "lg",
                  "cornerRadius": "30px"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 1
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "box",
                          "layout": "horizontal",
                          "contents": [
                            {
                              "type": "filler"
                            },
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [],
                              "width": "2px",
                              "backgroundColor": "#6486E3"
                            },
                            {
                              "type": "filler"
                            }
                          ],
                          "flex": 1
                        }
                      ],
                      "width": "12px"
                    },
                    {
                      "type": "text",
                      "text": "Walk",
                      "gravity": "center",
                      "flex": 4,
                      "size": "xs",
                      "color": "#8c8c8c"
                    }
                  ],
                  "spacing": "lg",
                  "height": "64px"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "終點",
                      "gravity": "center",
                      "size": "sm"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "filler"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [],
                          "cornerRadius": "30px",
                          "width": "12px",
                          "height": "12px",
                          "borderColor": "#6486E3",
                          "borderWidth": "2px"
                        },
                        {
                          "type": "filler"
                        }
                      ],
                      "flex": 0
                    },
                    {
                      "type": "text",
                      "text": "[成功校區] 成大博物館",
                      "gravity": "center",
                      "flex": 4,
                      "size": "sm"
                    }
                  ],
                  "spacing": "lg",
                  "cornerRadius": "30px"
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
                  "style": "primary",
                  "height": "sm",
                  "action": {
                    "type": "message",
                    "label": "集合地點",
                    "text": "成功湖側"
                  },
                  "color": "#52bb7d"
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [],
                  "margin": "sm"
                }
              ],
              "flex": 0
            }
          }
    ]
  })]
    
def testnear():
    return [TextSendMessage(
    text='請選擇',
    quick_reply=QuickReply(
    items=[
        QuickReplyButton(action=MessageAction(label='遠', text='要搭公車喔!流瀾小西腳')),
        QuickReplyButton(action=MessageAction(label='近', text='騎腳踏車就Ok光點西竹圍')),
    ]))]
     
def near1():
    return [FlexSendMessage(
    alt_text='Flex Message',
    contents=
    {"type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/275021891_1457108971400712_5469771149922491596_n.jpg?_nc_cat=104&ccb=1-6&_nc_sid=730e14&_nc_ohc=Ab-g1tXoWCAAX-StMiM&_nc_ht=scontent-tpe1-1.xx&oh=00_AT8ByymYyeLbULkcczddR0SkQIkHl35DFVjoInXmqfoVYg&oe=627D0C8D",
      "size": "full",
      "aspectRatio": "16:10",
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
          "text": "流瀾小西腳",
          "weight": "bold",
          "size": "xl"
        },
        {
          "type": "box",
          "layout": "baseline",
          "margin": "md",
          "contents": [
            {
              "type": "icon",
              "size": "sm",
              "url": "https://cdn-icons-png.flaticon.com/512/395/395841.png"
            },
            {
              "type": "icon",
              "size": "sm",
              "url": "https://cdn-icons.flaticon.com/png/512/4981/premium/4981785.png?token=exp=1652042019~hmac=42ed4e684132261f7da9a34491045df5"
            },
            {
              "type": "icon",
              "size": "sm",
              "url": "https://cdn-icons.flaticon.com/png/512/4545/premium/4545114.png?token=exp=1652042080~hmac=e1f85d024301fc73651e870bf675c9b2"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "margin": "lg",
          "spacing": "sm",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "Place",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 1
                },
                {
                  "type": "text",
                  "text": "700台南市中西區保安路",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "Time",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 1
                },
                {
                  "type": "text",
                  "text": "半日遊",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            }
          ]
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
          "style": "primary",
          "height": "sm",
          "action": {
            "type": "uri",
            "label": "路線介紹",
            "uri": "http://exptainan.liberal.ncku.edu.tw/index.php?option=module&lang=cht&task=showlist&id=708&index=9"
          },
          "color": "#c65e4b"
        },
        {
          "type": "button",
          "style": "primary",
          "height": "sm",
          "action": {
            "type": "message",
            "label": "集合地點",
            "text": "流瀾小西腳集合地點"
          },
          "color": "#c65e4b"
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [],
          "margin": "sm"
        }
      ],
      "flex": 0
    }
    }
    )]

def near2():
    return [FlexSendMessage(
    alt_text='Flex Message',
    contents=
    {"type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/275128527_1457109064734036_8419935475914525629_n.jpg?_nc_cat=106&ccb=1-6&_nc_sid=730e14&_nc_ohc=AG58UUf4o54AX8ej5h0&_nc_ht=scontent-tpe1-1.xx&oh=00_AT9eD_EzWt4aRmoWA8Obu-GoNyFZT6ikzLgeeUBJmAkD7g&oe=627D30F5",
      "size": "full",
      "aspectRatio": "16:10",
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
          "text": "光點西竹圍",
          "weight": "bold",
          "size": "xl"
        },
        {
          "type": "box",
          "layout": "baseline",
          "margin": "md",
          "contents": [
            {
              "type": "icon",
              "size": "sm",
              "url": "https://cdn-icons-png.flaticon.com/512/395/395841.png"
            },
            {
              "type": "icon",
              "size": "sm",
              "url": "https://cdn-icons.flaticon.com/png/512/4981/premium/4981785.png?token=exp=1652042019~hmac=42ed4e684132261f7da9a34491045df5"
            },
            {
              "type": "icon",
              "size": "sm",
              "url": "https://cdn-icons.flaticon.com/png/512/4545/premium/4545114.png?token=exp=1652042080~hmac=e1f85d024301fc73651e870bf675c9b2"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "margin": "lg",
          "spacing": "sm",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "Place",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 1
                },
                {
                  "type": "text",
                  "text": "701台南市東區育樂街197巷",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "Time",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 1
                },
                {
                  "type": "text",
                  "text": "半日遊",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            }
          ]
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
          "style": "primary",
          "height": "sm",
          "action": {
            "type": "uri",
            "label": "路線介紹",
            "uri": "http://exptainan.liberal.ncku.edu.tw/index.php?option=module&lang=cht&task=showlist&id=709&index=10"
          },
          "color": "#c65e4b"
        },
        {
          "type": "button",
          "style": "primary",
          "height": "sm",
          "action": {
            "type": "message",
            "label": "集合地點",
            "text": "光點西竹圍集合地點"
          },
          "color": "#c65e4b"
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [],
          "margin": "sm"
        }
      ],
      "flex": 0
    }
    }
    )]

def testfar():
    return [TextSendMessage(
    text='請選擇',
    quick_reply=QuickReply(
    items=[
        QuickReplyButton(action=MessageAction(label='動物', text='水乳交融')),
        QuickReplyButton(action=MessageAction(label='人文', text='走尋老月津')),
    ]))]

def far1():
    return [FlexSendMessage(
    alt_text='Flex Message',
    contents=
    {"type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/275049691_1457109001400709_1444572327883119844_n.jpg?_nc_cat=101&ccb=1-6&_nc_sid=730e14&_nc_ohc=1PjqpIqhFjEAX9SIpE9&_nc_oc=AQmfMabM2sN0iaqw-dJ-14n7K2V-wzEqQbX_A-fO-_s1u8U2_zWMeeZ3VrcYlM4xIZ4&_nc_ht=scontent-tpe1-1.xx&oh=00_AT_AFKw5pWMq9c11DMEqkInYRv8BUTbJih8sjC_wUarFdg&oe=627DE090",
      "size": "full",
      "aspectRatio": "16:10",
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
          "text": "水乳交融",
          "weight": "bold",
          "size": "xl"
        },
        {
          "type": "box",
          "layout": "baseline",
          "margin": "md",
          "contents": [
            {
              "type": "icon",
              "size": "sm",
              "url": "https://cdn-icons-png.flaticon.com/512/395/395841.png"
            },
            {
              "type": "icon",
              "size": "sm",
              "url": "https://cdn-icons-png.flaticon.com/512/2395/2395796.png"
            },
            {
              "type": "icon",
              "size": "sm",
              "url": "https://cdn-icons-png.flaticon.com/512/3267/3267610.png"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "margin": "lg",
          "spacing": "sm",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "Place",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 1
                },
                {
                  "type": "text",
                  "text": "六甲林鳳營、烏山頭水庫",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "Time",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 1
                },
                {
                  "type": "text",
                  "text": "全日遊",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            }
          ]
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
          "style": "primary",
          "height": "sm",
          "action": {
            "type": "uri",
            "label": "路線介紹",
            "uri": "http://exptainan.liberal.ncku.edu.tw/index.php?option=module&lang=cht&task=showlist&id=706&index=7"
          },
          "color": "#6ebbbd"
        },
        {
          "type": "button",
          "style": "primary",
          "height": "sm",
          "action": {
            "type": "message",
            "label": "集合地點",
            "text": "大路線集合地點"
          },
          "color": "#6ebbbd"
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [],
          "margin": "sm"
        }
      ],
      "flex": 0
    }
    }
    )]

def far2():
    return [FlexSendMessage(
    alt_text='Flex Message',
    contents=
    {"type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/275016424_1457108761400733_893547256470070660_n.png?_nc_cat=100&ccb=1-6&_nc_sid=730e14&_nc_ohc=P1dZdyIxsI4AX_oZZiT&_nc_ht=scontent-tpe1-1.xx&oh=00_AT8vXCJk_tqxLVm3jc50hnUYfuO_i0bTwSVZmRE8dIT-Lg&oe=627D912F",
      "size": "full",
      "aspectRatio": "16:10",
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
          "text": "走尋老月津",
          "weight": "bold",
          "size": "xl"
        },
        {
          "type": "box",
          "layout": "baseline",
          "margin": "md",
          "contents": [
            {
              "type": "icon",
              "size": "sm",
              "url": "https://cdn-icons-png.flaticon.com/512/395/395841.png"
            },
            {
              "type": "icon",
              "size": "sm",
              "url": "https://cdn-icons.flaticon.com/png/512/2397/premium/2397462.png?token=exp=1652045312~hmac=cc700a23977bfa826a70be62f15d5492"
            },
            {
              "type": "icon",
              "size": "sm",
              "url": "https://cdn-icons.flaticon.com/png/512/1048/premium/1048357.png?token=exp=1652045359~hmac=13b366cbff31cc85600b542111614e1f"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "margin": "lg",
          "spacing": "sm",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "Place",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 1
                },
                {
                  "type": "text",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5,
                  "text": "737台南市鹽水區月津路"
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "Time",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 1
                },
                {
                  "type": "text",
                  "text": "全日遊",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            }
          ]
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
          "style": "primary",
          "height": "sm",
          "action": {
            "type": "uri",
            "label": "路線介紹",
            "uri": "http://exptainan.liberal.ncku.edu.tw/index.php?option=module&lang=cht&task=showlist&id=707&index=8"
          },
          "color": "#6ebbbd"
        },
        {
          "type": "button",
          "style": "primary",
          "height": "sm",
          "action": {
            "type": "message",
            "label": "集合地點",
            "text": "大路線集合地點"
          },
          "color": "#6ebbbd"
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [],
          "margin": "sm"
        }
      ],
      "flex": 0
    }
    }
    )]

