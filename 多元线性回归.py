#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import time
import xlrd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import cross_val_predict

'''读取数据'''
def ReadFile(filePath):
    data = xlrd.open_workbook(filePath)
    table = data.sheet_by_name('相对密度')
    
    priceList = table.col_values(6)[1:] #任务标价
    nrows = table.nrows
    datasRel = []
    for i in range(1, nrows):
        datasRel.append(table.row_values(i)[1:6])#相对密度
    return np.array(datasRel), np.array(priceList)


def main():
    strFilePath = './用于决策树与回归的密度数据.xlsx'
    
    X, y = ReadFile(strFilePath)
    #X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    linreg = LinearRegression()
    #linreg.fit(X_train, y_train)
    linreg.fit(X, y)
    print("回归系数0："+str(linreg.intercept_))
    print("回归系数："+str(linreg.coef_))
    '''
    y_pred = linreg.predict(X_test)
    # 用scikit-learn计算MSE
    print ("MSE:"+str(metrics.mean_squared_error(y_test, y_pred)))
    # 用scikit-learn计算RMSE
    print ("RMSE:"+str(np.sqrt(metrics.mean_squared_error(y_test, y_pred))))
    '''
    # 10折交叉验证
    predicted = cross_val_predict(linreg, X, y, cv=10)
    # 用scikit-learn计算MSE
    print ("均方差MSE: "+str(metrics.mean_squared_error(y, predicted)))
    # 用scikit-learn计算RMSE
    print ("均方根差RMSE: "+str(np.sqrt(metrics.mean_squared_error(y, predicted))))
    
start = time.clock() 
main()
elapsed = (time.clock()-start)
print("run time: "+str(elapsed)+" s")