class fib(object):
	def __init__(self):
		self.a,self.b=0,1
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>20:
			raise StopIteration()
		return self.a

for n in fib():
	print(n)

