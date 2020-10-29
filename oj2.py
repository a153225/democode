import requests
from bs4 import BeautifulSoup
import xlwt
import time
# 获取第一页的内容


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return ''

# 解析第一页内容，数据结构化


def parse_one_page(html):

    soup = BeautifulSoup(html, 'html.parser')
    i = 0
    for item in soup.select('tr')[2:]:

        yield{
            'stu_name': item.select('div')[i].text,
            'stu_num': item.select('div')[i+1].text,
            'correct': item.select('div')[i+2].text,
            'total': item.select('div')[i+3].text,
            'correct_rate': item.select('div')[i+4].text,

        }


def write_to_excel():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('oj', cell_overwrite_ok=True)
    row0 = ["序号", "学号", "姓名", "正确", "总提交", "正确率"]
    # 写入表头
    for j in range(0, len(row0)):
        sheet1.write(0, j, row0[j])
    # 依次爬取每一页内容的每个人的信息，并将其依次写入Excel
    i = 0
    data = (time.strftime("%Y年%m月%d日%H时%M分%S秒", time.localtime(time.time())))
    for k in range(0, 51, 50):
        url = "http://acm.zzuli.edu.cn/ranklist.php?prefix=20209&start=%s" % (
            str(k))
        html = get_one_page(url)
        print('正在保存第%d页。' % k)
        # 写入每个人的信息
        for item in parse_one_page(html):
            sheet1.write(i+1, 0, i+1)
            sheet1.write(i+1, 1, item['stu_name'])
            sheet1.write(i+1, 2, item['stu_num'])
            sheet1.write(i+1, 3, item['correct'])
            sheet1.write(i+1, 4, item['total'])
            sheet1.write(i+1, 5, item['correct_rate'])
            i += 1

    f.save(r'D:\DeskTop\OJlist\oj排名%s.xls' % data)


def main():
    write_to_excel()


if __name__ == '__main__':
    main()
