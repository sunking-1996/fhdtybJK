# coding=utf-8

import xlrd

if __name__ == '__main__':

    # excel文件全路径
    xlPath = "C:\\Users\\think\\Desktop\\接口用例.xlsx"
    # 用于读取excel
    xlBook = xlrd.open_workbook(xlPath)
    # 获取excel工作簿数
    count = len(xlBook.sheets())
    print(u"工作簿数为:  ", count)
    # 获取 表 数据的行列数
    table = xlBook.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    print(u"表数据行列为(%d, %d)" % (nrows, ncols))
    # 循环读取数据
    for i in range(0, nrows):
        rowValues = table.row_values(i)  # 按行读取数据
        # 输出读取的数据
        for data in rowValues:
            print(data, " ",)
        print("")