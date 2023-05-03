class x:
    def __init__(self,a):
        self.a=a
    def dou(self):
        self.a*=2
class y(x):
    def __init__(self,a):
        x.__init__(self,a)
    def tri(self):
        self.a*=3
ob=y(5)
ob=x(4)
print(ob.a)
ob.dou()
print(ob.a)
ob.tri()
print(ob.a)
print(issubclass(ob,x))
print(isinstance(x,y))
