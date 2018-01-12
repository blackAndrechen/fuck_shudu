import datetime
import requests
from bs4 import BeautifulSoup as BS

class Fuck_shudu(object):
	def __init__(self,board):
		self.b = board   #数独，方便后面调用
		self.t = 0      #尝试的次数
	
	def check(self,x,y,value):  #测试数独是否符合规则，每行每列每宫数字不重复
		for row_item in self.b[x]:  #每行
			if row_item == value:
				return False
		for row_all in self.b:    #每列
			if row_all[y] == value:
				return False
		row,col = int(x/3)*3,int(y/3)*3   #判断该点属于哪宫
		row3col3 = self.b[row][col:col+3]+self.b[row+1][col:col+3]+self.b[row+2][col:col+3]
		for row3col3_item in row3col3:
			if row3col3_item == value:
				return False
		return True
	
	def get_next(self,x,y):  #得到下一个0点
		for next_soulu in range(y+1,9):
			if self.b[x][next_soulu] == 0:
				return x,next_soulu
		for row_n in range(x+1,9):
			for col_n in range(0,9):
				if self.b[row_n][col_n] == 0:
					return row_n,col_n
		return -1,-1
	
	def try_it(self,x,y): #破解函数，遍历每个0值，并循环填入值，尝试是否符合规则
		if self.b[x][y] == 0:
			for i in range(1,10):
				self.t += 1
				if self.check(x,y,i): #如果i符合，尝试设置(x,y) = i
					self.b[x][y] = i
					next_x,next_y = self.get_next(x,y) #得到下一0值的坐标
					if next_x == -1: #后面没有0值，破解成功
						return True
					else:
						end = self.try_it(next_x,next_y) #迭代，尝试填下一值
						if not end:  #not end 说明(x,y) = i 不符合
							self.b[x][y] = 0 #重新将(x,y)设置为0，并测试下一个i值是否符合条件
						else:
							return True
	
	def start(self):
		begin =datetime.datetime.now()
		if self.b[0][0] == 0:
			self.try_it(0,0)
		else:
			x,y = self.get_next(0,0)
			self.try_it(x,y)
		for i in self.b:
			print(i)
		end = datetime.datetime.now()
		print('cost time:{}'.format(end-begin)) #花费的时间（一般不会超过1s）和总次数
		print('try sum times:{}'.format(self.t))


class Crawl_shudu(object):
	def __init__(self,url):
		self.url = url

	def start(self):
		response = requests.get(self.url).text
		soup = BS(response,'lxml')
		sdbody = soup.find('table',class_='ptb')

		shudu = []
		for tr in sdbody.find_all('tr'):
			trnum = []
			for td in tr.find_all('td'):
				num = td.find('input')['value']
				if num == '':
					trnum.append(0)
				else:
					trnum.append(int(num))
			shudu.append(trnum)
		return shudu
	


