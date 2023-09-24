#这个是演示代码，学习请看explain_code

#请确保安装这两个外部库
from bs4 import BeautifulSoup
import requests
import numpy
#以下有3段测试代码：去掉注释就行，如果代码有问题请将文件改为英文

#这段代码为 拉取豆瓣top250电影的名称

# heads = {
#   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36"
# }
# for cent in range(0,250,25):
#     new_url = requests.get(f"https://movie.douban.com/top250??start={cent}",headers = heads).text
#     f=BeautifulSoup(new_url,"html.parser")
#     list_p = f.find_all("span",attrs={"class":"title"})
#     for getH in list_p:
#         if "/" in getH.string:
#             continue
#         else:
#             print(getH.string)

#这段代码为 拉取 books这个网站第一页的书的价格

# new_url=requests.get("http://books.toscrape.com/").text
# htmlGet=BeautifulSoup(new_url,"html.parser")
# getPrice=htmlGet.find_all("p",attrs={"class":"price_color"})
# for getP_W in getPrice:
#     print(getP_W.string)

#这段代码为 拉取 books这个网站第一页的书的名称

# new_url=requests.get("http://books.toscrape.com/")
# htmlGet=BeautifulSoup(new_url.text,"html.parser")
# getBnume=htmlGet.find_all("h3")
# for bookN in getBnume:
#     getBookN = bookN.find("a")
#     print(getBookN.string)

