import requests
from bs4 import BeautifulSoup
import xlwt
import time

#获取第一页的内容
def get_one_page(url):
 headers = {
   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
 }
 response = requests.get(url,headers=headers)
 if response.status_code == 200:
   return response.text
 return ''

#解析第一页内容，数据结构化
def parse_one_page(html):

   soup = BeautifulSoup(html,'lxml')
   i = 0
   for item in soup.select('ul')[1:0]:

       yield{
           'time':item.select('li')[i].text,
           'issue':item.select('li')[i+1].text,
           'digits':item.select('li')[i+2].text,
           'ten_digits':item.select('li')[i+3].text,
           'hundred_digits':item.select('li')[i+4].text,
           'single_selection':item.select('li')[i+5].text,
           #'group_selection_3':item.select('td')[i+4].text,
           #'group_selection_6':item.select('td')[i+5].text,
          #'sales':item.select('td')[i+6].text,
           #'return_rates':item.select('td')[i+7].text
     }

#将数据写入Excel表格中
def write_to_excel():
   f = xlwt.Workbook()                             
   sheet1 = f.add_sheet('3D',cell_overwrite_ok=True)
   row0 = ["开奖日期","期号","个位数","十位数","百位数","单数","组选3","组选6","销售额","返奖比例"]
   #写入第一行
   for j in range(0,len(row0)):
       sheet1.write(0,j,row0[j])
   
   #依次爬取每一页内容的每一期信息，并将其依次写入Excel
   i=0
   y=2011
   m=10
   for k in range(1,2):
       #url = 'http://kaijiang.zhcw.com/zhcw/html/3d/list_%s.html' %(str(k))
       url = 'http://lishi.tianqi.com/zhoukou/201803.html'
       html = get_one_page(url)
       print('正在保存第%d页。'%k)
       #写入每一期的信息
       for item in parse_one_page(html):
         sheet1.write(i+1,0,item['time'])
         sheet1.write(i+1,1,item['issue'])
         sheet1.write(i+1,2,item['digits'])
         sheet1.write(i+1,3,item['ten_digits'])
         sheet1.write(i+1,4,item['hundred_digits'])
         sheet1.write(i+1,5,item['single_selection'])
         sheet1.write(i+1,6,item['group_selection_3'])
         sheet1.write(i+1,7,item['group_selection_6'])
         sheet1.write(i+1,8,item['sales'])
         sheet1.write(i+1,9,item['return_rates'])
         i+=1
         #m=m+1
         #if m==12:
           #  y+=1
         
   f.save('weaher.xls')

def main():
   write_to_excel()

if __name__ == '__main__':
   main()
