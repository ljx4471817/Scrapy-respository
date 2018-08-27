import pickle #使用
from os import path
import jieba #使用分词功能
#matplotlib是python上的一个2D绘图库，它可以在夸平台上边出很多高质量的图像。
# 综旨就是让简单的事变得更简单，让复杂的事变得可能。
# 我们可以用matplotlib生成 绘图、直方图、功率谱、柱状图、误差图、散点图等
import matplotlib.pyplot as plt
#wordcloud  制作云图
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator



comment = []
#获取评论数据
with open (r'D:\邪不压正影评\xie_zheng_new21.txt',mode='r',encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        if len(row.split(',')) == 5:
            comment.append(row.split(',')[4].replace('\n', ''))

#非全模式分词,cut_all表示非全模式
comment_after_split = jieba.cut(str(comment),cut_all=False)

wl_space_split= " ".join(comment_after_split)
#导入背景图
backgroud_Image = plt.imread(r'D:\Desktop\云图\backgroud.png')
stopwords = STOPWORDS.copy()
print(" STOPWORDS.copy()",help(STOPWORDS.copy()))
#可以加多个屏蔽词
stopwords.add("电影")
stopwords.add("一部")
stopwords.add("一个")
stopwords.add("没有")
stopwords.add("什么")
stopwords.add("有点")
stopwords.add("这部")
stopwords.add("这个")
stopwords.add("不是")
stopwords.add("真的")
stopwords.add("感觉")
stopwords.add("觉得")
stopwords.add("还是")

#设置词云参数
#参数分别是指定字体/背景颜色/最大的词的大小,使用给定图作为背景形状
wc =WordCloud(width=1024,height=768,background_color='white',
              mask = backgroud_Image,font_path='rD:\Desktop\云图\STKAITI.TTF',
              stopwords=stopwords,max_font_size=400,
              random_state=50)
#将分词后数据传入云图
wc.generate_from_text(wl_space_split)
plt.imshow(wc)
plt.axis('off')#不显示坐标轴
plt.show()
#保存结果到本地
wc.to_file(r'D:\Desktop\云图\show.jpg')