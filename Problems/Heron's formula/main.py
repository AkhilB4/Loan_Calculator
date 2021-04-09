import math

a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
res = p * (p - a) * (p - b) * (p - c)
print(math.sqrt(res))
