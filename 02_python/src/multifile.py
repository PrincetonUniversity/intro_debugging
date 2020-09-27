"""There is no bug in this code."""

from MyShapes import RightTriangle

def myfunc1(x, y , z):
  mymin = min(x, y, z)
  mymax = max(x, y, z)
  return mymin * mymax

def myfunc2(x, y, mysum):
  z = myfunc1(x, y, mysum)
  return -z**2

x = sum([1 for u in '4a9d9eeJz' if u.isalpha()])
y = 1 if x > 7 else -1

mysum = 0
for i in range(10):
  mysum += i

print("myfunc2 = ", myfunc2(x, y, mysum))

mytriangle = RightTriangle(2.5, 7.0)
print("triangle area = ", mytriangle.area())
