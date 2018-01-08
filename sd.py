import datetime

class Solution(object):
	def __init__(self,board):
		self.b = board
		self.t = 0
	
	def check(self,x,y,value):
		for row_item in self.b[x]:
			if row_item == value:
				return False
		for row_all in self.b:
			if row_all[y] == value:
				return False
		row,col = int(x/3)*3,int(y/3)*3
		row3col3 = self.b[row][col:col+3]+self.b[row+1][col:col+3]+self.b[row+2][col:col+3]
		for row3col3_item in row3col3:
			if row3col3_item == value:
				return False
		return True
	
	def get_next(self,x,y):
		for next_soulu in range(y+1,9):
			if self.b[x][next_soulu] == 0:
				return x,next_soulu
		for row_n in range(x+1,9):
			for col_n in range(0,9):
				if self.b[row_n][col_n] == 0:
					return row_n,col_n
		return -1,-1
	
	def try_it(self,x,y):
		if self.b[x][y] == 0:
			for i in range(1,10):
				self.t += 1
				if self.check(x,y,i):
					self.b[x][y] = i
					next_x,next_y = self.get_next(x,y)
					if next_x == -1:
						return True
					else:
						end = self.try_it(next_x,next_y)
						if not end:
							self.b[x][y] = 0
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
		print('cost time:{}'.format(end-begin))
		print('try sum times:{}'.format(self.t))


