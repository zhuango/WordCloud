import jieba
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread

from weiboExtractor import *

# 微博文本
mytext = "发不出去微博 发不了图？ 这论文我编不下去了 哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈啊哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈​​​​"
mytext = weiboExtractor()
# 保存词云图片路径
saved = "./weiboCloud.jpg"
# 背景图片
bgPicture = "./mask.jpg"
# 背景颜色
bgColor = "white"
# 微软雅黑中文字体
microYaHei = "./msyh.ttf"

# 设置背景图片
alice_coloring = imread(bgPicture)
wordcloudGenerator = WordCloud(
    background_color= bgColor,  # 背景颜色
    mask=alice_coloring,        # 背景图片
    stopwords = STOPWORDS,      # 去掉停用词
    font_path = microYaHei,     # 字体
    max_font_size=60,           # 最大字体大小
    random_state = 20)

# 先对mytext进行分词，然后生成词云
wordcloud = wordcloudGenerator.generate(" ".join(jieba.cut(mytext)))

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
# 保存词云图片
plt.savefig(saved, dpi=600, right=0.45)
# 显示词云图片
plt.show()