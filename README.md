# CUMCMCoding 2017

## 一、运行说明

1. 环境：
    + macOS Sierra 10.12.5
    + Python 3.6.2
    + IPython 6.2.0
    + Anaconda Navigator 1.6.4, spyder 3.2.3
1. 使用的第三方库：（请先使用pip install 安装）
	+ matplotlib (2.0.2)
  	+ scikit-learn (0.19.0)
  	+ graphviz (0.8)
  	+ pydot (1.2.3)
 	+ xlrd (1.1.0)
  	+ xlwt (1.3.0)
1. 为确保程序读取数据无误，若使用命令行执行代码，请先确保进入当前目录。
1. graphviz可能需要使用brew安装，或其他办法解决路径问题。

## 二、py源程序文件说明
1. 统一说明：
 	+ 程序内含有计时模块，因此程序运行完后会打印运行时间。
 	+ 对于运行时间较长的程序已经在代码开头以注释方式写明大约运行时长。该时间受环境影响。
1. ***kNN求绝对和相对密度.py***
 	+ 用到**原始信息.xlsx**的数据，并会把结果在本目录下输出为一个```.xls```文件，该文件会含有两个sheet。
 	+ ```main()```函数中的oldOrNew为0则对已完成任务进行处理。oldOrNew为1则对新任务进行处理。因此运行前先自行修改。
1. ***决策树分类.py***
 	+ 用到**用于决策树与回归的密度数据.xlsx**的数据，并会把结果在本目录下输出一个中间文件和**DecideTree.pdf**文件，该文件是决策树的可视化。
 	+ 决策树的默认最大深度（即不剪枝处理）。也可以设置最大深度，在```main()```函数中有相应注释可以修改。
1. ***多元线性回归.py***
 	+ 用到**用于决策树与回归的密度数据.xlsx**的数据。
 	+ 结果输出回归系数，以及10折交叉验证的均方差和均方根差。
1. ***测试最佳价格方案.py***
 	+ 用到**用于决策树与回归的密度数据.xlsx**的数据。
 	+ 测试方法分两种，一种是给出文件让程度读入并测试，一种是根据前题结果计算价格并测试。默认使用第二种，使用枚举方法获得最佳系数。
 	+ 若只用文件数据测试，则文件格式和读入数据文件格式一致即可，并修改main()中相应注释的代码。
1. ***任务打包+价格修改+测试.py***
 	+ 用到**第三问编程数据.xlsx**或**第四问编程数据.xlsx**的数据。
 	+ ```main()```函数中的oldOrNew为0则对已完成任务进行处理。oldOrNew为1则对新任务进行处理，并分别导入不用的xlsx数据。因此运行前先自行修改。
 	+ 对于oldOrNew=1时，若想查看任务不打包时的测试结果，怎在```main()```函数中注释```kNNUpdatePrice(bigTable, k, p/10)```即可。此时输出结果也为多个，但不受p值影响，因此是同一个结果。

## 三、xlsx文件说明
1. ***原始信息.xlsx*** 是对附件1~3的精简处理，里面共对应三个sheet。
1. ***用于决策树与回归的密度数据.xlsx*** 是 **kNN求绝对和相对密度.py** 程序运行后数据整合的结果。
1. ***用于决策树与回归的密度数据.xlsx*** 用于生成决策树和多元线性回归，由2点文件整合而成。
1. ***第三问编程数据.xlsx*** 和 ***第四问编程数据.xlsx*** 也是由 **原始信息.xlsx** 和 **用于决策树与回归的密度数据.xlsx** 整合而成。

## 四、日志
1. 比赛结束当晚9.17初次完成，并用[MaHua](https://github.com/jserme/mahua)转化成```.html```，提交版是```.html```文档。后因考虑到查重所以删除了仓库。
2. 10.24，省赛结果已出，遗憾省二。重新整理回```.md```文件并commit。

## 五、参考资料
>排名不分先后
1. [python操作Excel读写--使用xlrd - lhj588 - 博客园](http://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html)
1. [Python--matplotlib绘图可视化知识点整理 - 潘凌昀的兴趣技术杂货铺 - CSDN博客](http://blog.csdn.net/panda1234lee/article/details/52311593)
1. [python中NumPy和Pandas工具包中的函数使用笔记（方便自己查找） - baoyan2015的博客 - CSDN博客](http://blog.csdn.net/baoyan2015/article/details/53503073)
1. [python中的sum函数.sum(axis=1) - yyxayz - 博客园](http://www.cnblogs.com/yyxayz/p/4033736.html)
1. [python实现根据两点经纬度计算实际距离 - TH_NUM的博客 - CSDN博客](http://blog.csdn.net/TH_NUM/article/details/51841052)
1. [Python 字典 列表 嵌套 复杂排序大全 - 木木_Ray的专栏 - CSDN博客](http://blog.csdn.net/ray_up/article/details/42084863)
1. [用Python实现K-近邻算法 - Python - 伯乐在线](http://python.jobbole.com/83794/)
1. [Python中numpy模块的tile()方法简单说明 - wy的点滴 - CSDN博客](http://blog.csdn.net/wy250229163/article/details/52453201)
1. [Python数据分析与挖掘实战--读书笔记 - 简书](http://www.jianshu.com/p/597dfcc3b448)
1. ["RuntimeError: Make sure the Graphviz executables are on your system's path" after installing Graphviz 2.38 | Stackoverflow Help | Query Starter](https://www.questarter.com/q/-quot-runtimeerror-make-sure-the-graphviz-executables-are-on-your-system-39-s-path-quot-after-installing-graphviz-2-38-27_35064304.html)
1. [Numpy and Scipy Documentation — Numpy and Scipy documentation](https://docs.scipy.org/doc/)
1. [1.10. Decision Trees — scikit-learn 0.19.0 documentation](http://scikit-learn.org/stable/modules/tree.html#tree-classification)
1. [sklearn.linear_model.LogisticRegression — scikit-learn 0.19.0 documentation](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression)
1. [用scikit-learn和pandas学习线性回归 - 刘建平Pinard - 博客园](http://www.cnblogs.com/pinard/p/6016029.html)
1. [Sklearn-train_test_split随机划分训练集和测试集 - Cherzhoucheer的博客 - CSDN博客](http://blog.csdn.net/cherdw/article/details/54881167)
1. [使用graphviz画关系图](http://freewind.in/posts/1745-use-graphviz-to-draw-relationship/)
1. [详细记录python的range()函数用法 - xxd - 博客园](http://www.cnblogs.com/buro79xxd/archive/2011/05/23/2054493.html)
1. [Python如何克隆或复制列表(list)？ - 共享笔记](https://gxnotes.com/article/8850.html)
1. [python - Can't catch mocked exception because it doesn't inherit BaseException - Stack Overflow](https://stackoverflow.com/questions/31713054/cant-catch-mocked-exception-because-it-doesnt-inherit-baseexception)
1. [Python补充05 字符串格式化 (%操作符) - Vamei - 博客园](http://www.cnblogs.com/vamei/archive/2013/03/12/2954938.html)
1. [MaHua 在线markdown编辑器](http://mahua.jser.me/)
1. [Python--matplotlib绘图可视化知识点整理 - 止战 - 博客园](http://www.cnblogs.com/zhizhan/p/5615947.html)
