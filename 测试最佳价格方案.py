#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
遍历找最有优k1，k2的测试方案预估时间：290.6369049999994 s
'''

from sklearn import tree
import numpy as np
import xlrd
import time
import copy

'''读取文件坐标'''
def ReadFile(filePath):
    # 表一:已完成的表
    data = xlrd.open_workbook(filePath)
    table = data.sheet_by_name('相对密度')
    
    comList = table.col_values(7)[1:] #执行情况
    nrows = table.nrows
    datasRel = []
    for i in range(1, nrows):
        datasRel.append(table.row_values(i)[1:7])#相对密度和标价
    return np.array(datasRel), np.array(comList)

'''直接读取测试数据读取'''
def ReadFile2(filePath):
    # 表一:已完成的表
    data = xlrd.open_workbook(filePath)
    table = data.sheet_by_name('相对密度')

    nrows = table.nrows
    datasRel = []
    for i in range(1, nrows):
        datasRel.append(table.row_values(i)[1:7])#相对密度和标价
    return np.array(datasRel)

'''读取X2，X3用于计算价格，其他同取'''
def ReadFile3(filePath):
    # 表一:已完成的表
    data = xlrd.open_workbook(filePath)
    table = data.sheet_by_name('相对密度')
    
    x2 = table.col_values(3)[1:] #限额
    x3 = table.col_values(4)[1:] #时间
    
    nrows = table.nrows
    datasRel = []
    for i in range(1, nrows):
        datasRel.append(table.row_values(i)[1:6])#相对密度，标价自己设
    return datasRel, np.array(x2), np.array(x3)#dataRel不要返回narray，因为后期要追加

def main():
    strFilePath = './用于决策树与回归的密度数据.xlsx'
    
    reldata, target = ReadFile(strFilePath)
    clfrel = tree.DecisionTreeClassifier()#可以设置最大深度
    clfrel.fit(np.array(reldata), np.array(target))
    
    result_max = 0
    result_max_k = []
    
    date_no_price, x2, x3 = ReadFile3(strFilePath)
    #若计数相同则记录最后一个k
    for k1 in range(1, 201):#实际区间是(0,20]，刻度为0.1
        for k2 in range(1, 201):
            datetest = []
            datetest = copy.deepcopy(date_no_price)#不能直接等于，列表时引用类型
            xx2 = k1/10 * (x2 - 0.589)
            xx3 = k2/10 * (x3 - 0.884)
            z = []
            z = xx2 + xx3 + 67.25
            for i in range(len(z)):
                datetest[i].append(z[i])
            res = clfrel.predict(np.array(datetest))#预测
            #统计
            count = 0
            for i in range(len(res)):
                if(res[i]==1):
                    count += 1
            print("k1=%f, k2=%f, count=%d" % (k1/10, k2/10, count))
            if(count > result_max):
                result_max = count
                result_max_k = [k1/10, k2/10]
    print("测试集中完成的人数：%d" % (result_max))
    print("此时k1，k2值分别为：%r" % (result_max_k))
    
    
    '''已经给出数据表的测试处理
    path1= '/Users/littlesec/Downloads/已结束项目处理数据2.xlsx'
    testList = ReadFile2(path1)
    res = clfrel.predict(testList)
    #print(res)
    count = 0
    for i in range(len(res)):
        if(res[i]==1):
            count += 1
    print(count)
    '''
    
start = time.clock() 
main()
elapsed = (time.clock()-start)
print("run time: "+str(elapsed)+" s")