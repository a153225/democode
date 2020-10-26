import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import xlwt
import time

url = "http://acm.zzuli.edu.cn/ranklist.php?prefix=20209&start=strval(0)"
page = requests.get(url, timeout=30)
page2 = BeautifulSoup(page.text, 'html.parser')
# print(page2)
f = xlwt.Workbook()
sheet1 = f.add_sheet('oj', cell_overwrite_ok=True)
row0 = ["序号", "学号", "姓名", "正确", "总提交", "正确率"]
for j in range(0, len(row0)):
    sheet1.write(0, j, row0[j])

for item in page2.select('tr')[2:]:
    for item1 in item.select("td"):
        print(item1.select('div'))


f.save('oj.xls')
