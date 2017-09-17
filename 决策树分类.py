#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn import tree
import numpy as np
import xlrd
import graphviz
import time

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

def main():
    strFilePath = './用于决策树与回归的密度数据.xlsx'
    
    reldata, target = ReadFile(strFilePath)
    clfrel = tree.DecisionTreeClassifier(max_depth=6)#可以设置最大深度
    clfrel.fit(np.array(reldata), np.array(target))
    
    dot_data_rel = tree.export_graphviz(clfrel, out_file=None, class_names = ['未完成','完成'], special_characters=True) 
    graph_rel = graphviz.Source(dot_data_rel) 
    graph_rel.render("./DecideTree")

start = time.clock() 
main()
elapsed = (time.clock()-start)
print("run time: "+str(elapsed)+" s")