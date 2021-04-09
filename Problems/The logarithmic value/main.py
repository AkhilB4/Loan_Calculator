import math

a, b = int(input()), int(input())
print(round(math.log(a), 2) if b <= 0 or b == 1 else
      round(math.log(a, b), 2))
