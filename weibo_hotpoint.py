#-*-coding:utf-8-*-


from lxml import etree
import requests
import xlrd,xlwt


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

url = 'https://s.weibo.com/top/summary?Refer=top_hot'
base_link = 'https://s.weibo.com'

def get_detail():
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    trs = html.xpath("//tbody//tr")
    points = []
    for index,tr in enumerate(trs):
        xuhao = tr.xpath(".//td[@class='td-01 ranktop']")
        if xuhao == []:
            xuhao = '我在飙升，序号不明'
        else:
            xuhao = tr.xpath(".//td[@class='td-01 ranktop']/text()")[0]
        link = tr.xpath(".//td//a/@href")[0]
        true_link =base_link + link
        keyword = tr.xpath(".//td//a/text()")[0]
        numbers = tr.xpath(".//td/span/text()")
        if numbers == []:
            numbers = '无人关注'
        else:
            numbers = tr.xpath(".//td/span/text()")[0]
        hot_level = tr.xpath(".//td[@class='td-03']/i")
        if hot_level == []:
            hot_level = '无'
        else:
            hot_level = tr.xpath(".//td[@class='td-03']/i/text()")[0]

        point = {
            '序号':xuhao,
            '关键词':keyword,
            '链接':true_link,
            '关注人数':numbers,
            '推荐指数':hot_level
        }
        points.append(point)
    return points


head = ['序号','关键词','链接','关注人数','推荐指数']

def init_excel(workbook):
    sheet = workbook.add_sheet('微博热搜')
    for h in range(len(head)):
        sheet.write(0,h,head[h])
    return sheet

def save_data(points,sheet):
    for m in range(len(points)):
        h = m +1
        for l in range(len(head)):
            cell = points[m].get(head[l])
            sheet.write(h,l,cell)
    workbook.save('d:/微博热搜.xls')



if __name__ == '__main__':
    workbook = xlwt.Workbook(encoding='utf-8')
    points = get_detail()
    sheet = init_excel(workbook)
    save_data(points,sheet)
    print('Excel文件存在D盘，您可查看最新微博热点')
