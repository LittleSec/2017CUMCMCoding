#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import xlrd
import xlwt
import time
from math import *

'''
预计运行时间：
已完成任务：132.96701199999995s
新任务：223.91732699999997s
'''

'''根据经纬度计算两点实际距离km'''
def CulDisFromLL(pointA, pointB):
    radlat1 = radians(pointA[0])  
    radlat2 = radians(pointB[0])  
    a = radlat1-radlat2  
    b = radians(pointA[1]) - radians(pointB[1])  
    s = 2 * np.arcsin(sqrt(pow(np.sin(a/2),2) + cos(radlat1) * cos(radlat2) * pow(sin(b/2),2))) 
    earth_radius=6378.137  
    s = s * earth_radius  
    if(s < 0):  
        return -s  
    else:  
        return s

'''
读取文件坐标
oldOrNew参数：0:‘已完成任务’，1:‘新任务’
'''
def ReadFileLocation(fileName, oldOrNew):
    # 已完成任务表
    data = xlrd.open_workbook(fileName)
    if(oldOrNew == 0):
        tableA = data.sheet_by_name('已完成任务')
    else:
        tableA = data.sheet_by_name('新任务')
    WeiList = tableA.col_values(1) #纬度
    JingList = tableA.col_values(2) #经度
    nrows = tableA.nrows
    APointList = []
    for i in range(1, nrows):
        tempX = float(WeiList[i])
        tempY = float(JingList[i])
        APointList.append([tempX, tempY])
    
    WeiList = []
    JingList = []
    # 会员信息表
    tableB = data.sheet_by_name('会员信息')
    WeiList = tableB.col_values(1) #纬度
    JingList = tableB.col_values(2) #经度
    listWeight = []
    nrows = tableB.nrows
    BPointList = []
    for i in range(1, nrows):
        tempX = float(WeiList[i])
        tempY = float(JingList[i])
        BPointList.append([tempX, tempY])
    return np.array(APointList), np.array(BPointList)

'''
读取文件属性列
weightB参数用于获取会员信息表中附加属性，即kNN中出现频率的量度属性
3-任务限额
4-任务开始时间
5-信誉值
'''
def ReadFileWeight(fileName, weightB):
    # 已完成任务表
    data = xlrd.open_workbook(fileName)
    # 会员信息表
    tableB = data.sheet_by_name('会员信息')
    listWeight = tableB.col_values(weightB)[1:] #相对时间
    return np.array(listWeight)

'''默认出现频率衡量度为距离的kNN'''
def AbskNNAlgorithm(X, y, k):
    kNN = []
    ySize = y.shape[0]
    XSize = X.shape[0]
    #对X（已完成任务）中每个元素进行knn
    for i in range(XSize):
        distances = []
        for j in range(ySize):
            distances.append(float(CulDisFromLL(X[i], y[j])))
        distances.sort()#升序
        Ksum = 0
        for l in range(1, k+1):
            Ksum = Ksum + distances[l]
        if(Ksum == 0): #为了防止除以0
            kNN.append(float('inf'))
            continue
        kNN.append(k/Ksum)
    return kNN

'''带出现频率衡量度的绝对密度'''
def AbskNNAlgorithmWithWeight(X, y, listWeight, k):
    kNN = []
    ySize = y.shape[0]
    XSize = X.shape[0]
    #对X（已完成任务）中每个元素进行knn
    for i in range(XSize):
        distances = []
        for j in range(ySize):
            distances.append([float(CulDisFromLL(X[i], y[j])), listWeight[j]])
        distances.sort(key=lambda x: x[0])#对距离升序
        Ksum = 0
        for l in range(k):
            Ksum = Ksum + distances[l][1]
        kNN.append(k/Ksum)
    return kNN

'''相对密度的分子部分，即对密度求kNN'''
def RelakNN(dataSet, k):
    kNN = []
    dataSetSize = dataSet.shape[0]
    for i in range(dataSetSize):
        distances = []
        for j in range(dataSetSize):
            distances.append([float(CulDisFromLL(dataSet[i][0], dataSet[j][0])), dataSet[j][1]])
        distances.sort(key=lambda x: x[0])
        Ksum = 0
        for l in range(1, k+1):
            Ksum = Ksum + distances[l][1]
        kNN.append(Ksum/k)
    return kNN    

'''
把数据写入xls
oldOrNew参数：0:‘已完成任务’，1:‘新任务’
'''
def WriteDataInXls(abskNN, relkNN, oldOrNew):
    workbook = xlwt.Workbook() 
    sheet1 = workbook.add_sheet("绝对密度")
    sheet1.write(0, 0, "绝对任务密度")
    sheet1.write(0, 1, "绝对会员密度")
    sheet1.write(0, 2, "绝对限额密度")
    sheet1.write(0, 3, "绝对时间密度")
    sheet1.write(0, 4, "绝对信誉度密度")
    
    # kNN列表是一个5行*很多列的矩阵
    for j in range(len(abskNN)):#循环次数为5
        for i in range(len(abskNN[j])):
            sheet1.write(i+1, j, abskNN[j][i])
    
    sheet2 = workbook.add_sheet("相对密度")
    sheet2.write(0, 0, "相对任务密度")
    sheet2.write(0, 1, "相对会员密度")
    sheet2.write(0, 2, "相对限额密度")
    sheet2.write(0, 3, "相对时间密度")
    sheet2.write(0, 4, "相对信誉度密度")
    for j in range(len(relkNN)):
        for i in range(len(relkNN[j])):
            sheet2.write(i+1, j, relkNN[j][i])
            
    if(oldOrNew == 0):
        workbook.save("./kNN求密度数据（已完成任务）.xls")
    else:
        workbook.save("./kNN求密度数据（新任务）.xls")

def main():
    strFilePath = './原始信息.xlsx'
    k = 7 #k不能为0！
    oldOrNew = 1 #oldOrNew参数：0:‘已完成任务’，1:‘新任务’
    
    a, b = ReadFileLocation(strFilePath, oldOrNew)
    
    # 求绝对密度
    kNNabs = [] #0任务，1会员，2限额，3时间，4信誉
    kNNabs.append(AbskNNAlgorithm(a, a, k))
    kNNabs.append(AbskNNAlgorithm(a, b, k))
    for i in range(3, 6):
        c = ReadFileWeight(strFilePath, i)
        kNNabs.append(AbskNNAlgorithmWithWeight(a, b, c, k))
    
    # kNN列表是5*多维的矩阵
    
    #求相对密度
    kNNrels = [] #0任务，1会员，2限额，3时间，4信誉
    for i in range(len(kNNabs)):  
        kNNrel = []
        tempDataSet = []
        for j in range(len(kNNabs[i])):
            tempDataSet.append([a[j], kNNabs[i][j]])
        tempkNNRel = RelakNN(np.array(tempDataSet), k)
        for j in range(len(kNNabs[i])):
            if(kNNabs[i][j]==float('inf')):
                kNNrel.append(0.0)
                continue
            kNNrel.append(tempkNNRel[j]/kNNabs[i][j])
        kNNrels.append(kNNrel)
    
    WriteDataInXls(kNNabs, kNNrels, oldOrNew)

start = time.clock() 
main()
elapsed = (time.clock()-start)
print("run time: "+str(elapsed)+" s")
