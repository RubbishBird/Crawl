#-*-coding:utf-8-*-

import xlrd
import xlwt
import random
import pandas as pd
# 1、读取数据
# workbook = xlrd.open_workbook('import_sku (1).xls')
# # sheets = workbook.sheet_names()
# # print(sheets)
#
# sheet0 = workbook.sheet_by_index(0)
# # print("行数：%d" % sheet0.nrows)
# # print("列数：%d" % sheet0.ncols)
#
# cells = sheet0.row_slice(1,0,sheet0.ncols)
# for col in cells:
#     print(col.value)
#
# print("="*30)
# cells2 = sheet0.col_slice(0,0,sheet0.nrows)
# for row in cells2:
#     print(row)


# 2、写入数据
# workbook = xlwt.Workbook(encoding='utf-8')
# sheet = workbook.add_sheet('成绩表')
#
# sheet.write(0,0,'语文')
# sheet.write(0,1,'数学')
# sheet.write(0,2,'英语')
#
# for row in range(1,11):
#     for col in range(0,3):
#         sheet.write(row,col,random.randint(80,100))
# workbook.save('score.xls')


# 3、编辑数据
def edit_excel():
    rwd = xlrd.open_workbook("scores1.xls")
    sheet0 = rwd.sheet_by_index(0)
    # 获取当前excel所有的行
    nrows = sheet0.nrows
    # 获取当前excel所有的列
    ncols = sheet0.ncols
    # 添加列名称为总分的cell
    sheet0.put_cell(0,4,xlrd.XL_CELL_TEXT,'总分',None)
    # 添加行名称为平均分的cell
    sheet0.put_cell(nrows,0,xlrd.XL_CELL_TEXT,'平均分',None)

# 给学生名称的列，每行添加数据
# name = ['李白','关羽','荆轲','蔡文姬','赵云','张飞','诸葛亮','曹操','张良','许褚','刘备']
# for row in range(1,nrows):
#     sheet0.put_cell(row,3,xlrd.XL_CELL_TEXT,name[row],None)

    # 计算每个学生的总分
    # for row in range(1,nrows):
    #     AllScore = sheet0.row_values(row,0,3)
    #     sheet0.put_cell(row,4,xlrd.XL_CELL_TEXT,sum(AllScore),None)

    # 计算班级的平均分
    for col in range(1,ncols):
        scores = sheet0.col_values(col,1,nrows)
        print(scores)
        avgscore = sum(scores) / len(scores)
        sheet0.put_cell(nrows,col,xlrd.XL_CELL_TEXT,avgscore,None)

    # 新建一个sheet去保存上面修改的数据
    wwb = xlwt.Workbook(encoding='utf-8')
    newsheet = wwb.add_sheet('newscore')
    for row in range(0,sheet0.nrows):
        for col in range(sheet0.ncols):
            value = sheet0.cell_value(row,col)
            newsheet.write(row,col,value)
    wwb.save("newscores.xls")

def exchange_col():
    df = pd.read_excel('newscores.xls')
    df = df[['学生名称','语文','数学','英语','总分']]
    df.to_excel('scores1.xls',index=False)

if __name__ == '__main__':
    edit_excel()
    # exchange_col()