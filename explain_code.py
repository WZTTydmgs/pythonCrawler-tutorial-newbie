from bs4 import BeautifulSoup
import requests
#外部包不解释

#代码原理是通过 requests 这个包的函数来进行网页代码的拉取
#然后通过用 beautifulsoup 这个包对拉取的 requests 的对象进行解析为html
#最后对HTML 网页的代码进行标签查找就能 找到对应的数据
#对数据进行输出就行

#解释：
#以books网站的书名为例
new_url=requests.get("http://books.toscrape.com/")#得到网站
textGet=new_url.text#解析为TEXT格式
htmlGet=BeautifulSoup(textGet,"html.parser")#解析为html
getPrice=htmlGet.find_all("p",attrs={"class":"price_color"})
#这个为搜索对应的html标签,返回一个可以迭代的访问数据类型
for P_behavior in getPrice:
    print(P_behavior.string)
#这里可以把string去掉看效果

#其他代码大致也是这样
#如果有问题可以联系discord：...哥们好像上不去
#QQ：3032259354
