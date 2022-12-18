class A(object):
	def go(self):
		print "Go A Go"

class B(A):
	def go(self):
		super(B, self).go()
		print "GO B Go"

class C(A):
	def go(self):
		super(C, self).go()
		print "Go C Go"

class D(B, C):
	def go(self):
		super(D, self).go()
		print "go D go"

print "DDDDDDD"
d=D()
d.go()
