class A(object):
	def go(self):
		print('A')

class B(A):
	def go(self):
		super(B, self).go()
		print('B')

class C(A):
	def go(self):
		super(C, self).go()
		print('C')

class D(B, C):
	def go(self):
		super(D, self).go()
		print('D')


a = A()
a.go()

b = B()
b.go()

#d = D()
#d.go()