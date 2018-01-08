# 用python抓取https://www.oubk.com/上的数独并破解

## 用法
下载到本地，cmd到该目录
![](https://github.com/blackAndrechen/fuck_shudu/blob/master/pic/%E6%8D%95%E8%8E%B7.PNG)

在ipython环境，导入两文件，input数独页面的网址(这里只支持抓取不需登陆的数独网址)
![](https://github.com/blackAndrechen/fuck_shudu/blob/master/pic/%E6%8D%95%E8%8E%B71.PNG)

上者抓取的数独返回list，将给list传递给sd.Solution()类，并调用start()开始破解
![](https://github.com/blackAndrechen/fuck_shudu/blob/master/pic/%E6%8D%95%E8%8E%B72.PNG)