
def weiboExtractor():
    mytext = ""
    # 分析微博网页特征，以下字符串下一行即为微博文本， “0xAC” 是微博ID
    keyString = "<div class=\"WB_text W_f14\" node-type=\"feed_list_content\" nick-name=\"{}\">".format("0xAC")
    weibotext = "./weibo.txt"
    weiboS = open(weibotext, 'w')
    for i in range(1, 7):
        with open("./weibo/weibo{}.html".format(i)) as f:
            for line in f:
                if keyString in line.strip():
                    # 读取微博文本
                    text = f.readline().strip()
                    # 去掉该行微博文本意外的字符串
                    if "<" in text:
                        text = text.split("<")[0]
                    if "&#" in text:
                        text = text.split("&#")[0]
                    text = text.strip()
                    mytext += " " + text
                    if text != "":
                        weiboS.write(text.strip() + "\n")
    weiboS.close()
    return mytext
