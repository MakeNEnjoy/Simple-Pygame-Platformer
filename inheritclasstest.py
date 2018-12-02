class out:
	def __init__(self, x):
		self.x = x
	def test(self):
		print('Hello World')
class ins(out):
	def __init__(self, x, y):
		out.__init__(self, x)
		self.y = y
	def prints(self):
		print('x:', self.x)
		print('y:', self.y)
thing = ins(1,2)
thing.prints()
thing.test()