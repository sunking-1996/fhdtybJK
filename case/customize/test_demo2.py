# coding=utf-8
# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
Created on 2019-5-20
@author: 北京-宏哥
Project:学习和使用python读取Excel
'''
# 3.导入模块
import xlrd

if __name__ == '__main__':
    # 打开 exlce 表格，参数是文件路径
    data = xlrd.open_workbook('C:\\Users\\think\\Desktop\\接口用例.xlsx')
    #table = data.sheets()[0] # 通过索引顺序获取
    #table = data.sheet_by_index(0) # 通过索引顺序获取
    table = data.sheet_by_name(u'Sheet1')  # 通过名称获取
    nrows = table.nrows  # 获取总行数
    ncols = table.ncols  # 获取总列数
    # 获取一行或一列的值，参数是第几行
    print(table.row_values(0)) # 获取第一行值
    print(table.col_values(0)) # 获取第一列值
    print("pass")
    print("pass12")