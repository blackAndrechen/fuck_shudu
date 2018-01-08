# 用python抓取https://www.oubk.com/上的数独并破解

## 破解方法

将数独转化为一个9维的数组，其中空值设置为0，从第一个0值开始尝试填入（1-9），判断是否符合数独的规则，每行每列每宫不重复，符合则迭代寻找下一0值，并继续尝试填入数字，若无符合的数字，则返回上一数字并+1，继续测试，直到破解为止，该过程一般需要几万次尝试，但花费总时间不会超过1s


## 用法
下载到本地，cmd到该目录
![](https://github.com/blackAndrechen/fuck_shudu/blob/master/pic/%E6%8D%95%E8%8E%B7.PNG)

在ipython环境，导入两文件，input数独页面的网址(这里只支持抓取不需登陆的数独网址)
![](https://github.com/blackAndrechen/fuck_shudu/blob/master/pic/%E6%8D%95%E8%8E%B71.PNG)

上者抓取的数独返回list，将给list传递给sd.Solution()类，并调用start()开始破解
![](https://github.com/blackAndrechen/fuck_shudu/blob/master/pic/%E6%8D%95%E8%8E%B72.PNG)