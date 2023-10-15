import mysql.connector
import requests
import csv
from lxml import etree

# 建立数据库连接
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="040603",
    database="itds"
)
cursor = db_connection.cursor()
# 创建数据表
create_table_query = """
CREATE TABLE IF NOT EXISTS MOVIE (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
)
"""
cursor.execute(create_table_query)

insert_data_query = "INSERT INTO MOVIE (name) VALUES (%s)"

#打开CSV文件填入数据
with open('move_data.csv','w',newline='',encoding='utf-8') as fp:
    writer = csv.writer(fp)

    #先定义要爬取的字段
    writer.writerow(('name','actor','information','date','star','evaluate','introduction'))

    #定义要爬取的链接及设置 header 相关参数
    urls = ['https://movie.douban.com/top250?star={}&filter='.format(str(i)) for i in range(0,250,25)]
    headers={'User-Agent':'Mozilla/5.0 {x11; Linux x86_64} AppleWebKit/537.36 (KHTML,like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36'}

    #通过request请求访问网页并获取网页内容
    for url in urls:
        html = requests.get(url,headers=headers)
        selector = etree.HTML(html.text)
        infos = selector.xpath("//ol[@class='grid_view']/li")#visit all the URLs and get information

        #解析网页内容
        for info in infos:
            name = info.xpath(".//div[@class='item']//div[@class='hd']//a/span[1]/text()")
            #names = ''.join(name)

            #将获取的数据写入csv文件
            writer.writerow((name))
            cursor.execute(insert_data_query, (name))
            # 提交更改
            db_connection.commit()

# 关闭游标和数据库连接
cursor.close()
db_connection.close()

