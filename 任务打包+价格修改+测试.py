#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from sklearn import tree
import xlrd
import time
from math import *

'''
预计运行时间：
ordOrNew = 0，已完成任务：67.26664800000003 s
ordOrNew = 1，新任务：210.70983800000002 s
'''

'''根据经纬度计算两点实际距离km'''
def CulDisFromLL(pointA, pointB):
    radlat1 = radians(pointA[0])  
    radlat2 = radians(pointB[0])  
    a = radlat1 - radlat2  
    b = radians(pointA[1]) - radians(pointB[1])  
    s = 2 * np.arcsin(sqrt(pow(np.sin(a/2),2) + cos(radlat1) * cos(radlat2) * pow(sin(b/2),2))) 
    earth_radius=6378.137  
    s = s * earth_radius  
    if(s < 0):  
        return -s  
    else:  
        return s

'''读取文件数据'''
def ReadFileLocation(fileName, oldOrNew):
    data = xlrd.open_workbook(fileName)
    sheet1 = data.sheets()[0]
    nrows = sheet1.nrows
    
    bigTable = []
    for i in range(1, nrows):
        tempDenPri = sheet1.row_values(i)[1:7] #密度和价格
        if(oldOrNew == 1):#新任务需要先算价格
            tempDenPri[5] = 4.4*(tempDenPri[2]-0.589) + 3.5*(tempDenPri[3]-0.884) + 67.25
        tempLoc = sheet1.row_values(i)[8:10] #纬经度
        bigTable.append([tempDenPri, tempLoc])
    # [[[密度和价格],[坐标]], [[密度和价格],[坐标]], ..., [[密度和价格],[坐标]] ]
    
    return bigTable

'''
默认出现频率衡量度为距离的kNN
bigTable的格式：[[[密度和价格],[坐标]], [[密度和价格],[坐标]], ..., [[密度和价格],[坐标]] ]
'''
def kNNUpdatePrice(bigTable, k, p):
    nrows = len(bigTable)
    for i in range(nrows):
        X = bigTable[i] #X的格式：[[密度和价格],[坐标]]
        if(X[0][0] < p):
            distances = []
            for i in range(nrows):
                distances.append([float(CulDisFromLL(X[1], bigTable[i][1])), bigTable[i][0][5]])
            distances.sort(key=lambda x: x[0])#对距离升序
            tempPrice = 0
            for i in range(1, k+1): #自身距离为0
                tempPrice += distances[i][1]
            newPrice = (X[0][5] + tempPrice) / (k + 1)
            X[0][5] = newPrice #修改价格

def DecisionTree():
    filePath = './用于决策树与回归的密度数据.xlsx'
    data = xlrd.open_workbook(filePath)
    table = data.sheet_by_name('相对密度')
    comList = table.col_values(7)[1:] #执行情况
    nrows = table.nrows
    datasRel = []
    for i in range(1, nrows):
        datasRel.append(table.row_values(i)[1:7])#相对密度和标价
    
    reldata = np.array(datasRel)
    target = np.array(comList)

    clfrel = tree.DecisionTreeClassifier()
    clfrel.fit(np.array(reldata), np.array(target))
    return clfrel

def main():
    strFilePath = ''
    rangeList = []
    k = 7 #k不能为0！
    oldOrNew = 1 #oldOrNew参数：0:‘已完成任务’，1:‘新任务’
    clf = DecisionTree()
    
    if(oldOrNew == 0):
        strFilePath = './第三问编程数据.xlsx'
        rangeList = list(range(8, 31))#实际为[0.8,3.0]
    else:
        strFilePath = './第四问编程数据.xlsx'
        rangeList = list(range(1, 21))#实际为[0.1,2.0]
    
    for p in rangeList:
        bigTable = ReadFileLocation(strFilePath, oldOrNew)
        nrows = len(bigTable)
        kNNUpdatePrice(bigTable, k, p/10)
        testList = []
        for i in range(nrows):
            testList.append(bigTable[i][0])
        res = clf.predict(np.array(testList))
        count = 0
        for i in range(len(res)):
            if(res[i]==1):
                count += 1
        print("此时p为%f，测试完成数为%d，完成率为：%f" % (p/10, count, count/nrows))
    
start = time.clock() 
main()
elapsed = (time.clock()-start)
print("run time: "+str(elapsed)+" s")
