class A(object):
	def go(self):
		print "Go A Go"
	def stop(self):
		print "Stop A Stop"
	def pause(self):
		raise Exception ("Not Implemented")

class B(A):
	def go(self):
		super(B, self).go()
		print "GO B Go"
	def stop(self):
#		super(B, self).stop()
		print "Stop B Stop"
	def pause(self):
		print "pause"

class C(A):
	def go(self):
		super(C, self).go()
		print "Go C Go"
	def stop(self):
		print "stop C stop"

class D(B, C):
	def go(self):
		super(D, self).go()
		print "go D go"
	def stop(self):
		print "stop D stop"
a=A()
a.go()
a.stop()
#a.pause()

print "BBBBB"
b=B()
b.go()
b.stop()

print "CCCCC"
c=C()
c.go()
c.stop()

print "DDDDDDD"
d=D()
d.go()
d.stop()
d.pause()
