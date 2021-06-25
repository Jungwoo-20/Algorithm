import sys
import math
n = math.sqrt(int(sys.stdin.readline()))
if n.is_integer():
    print(int(n))
else:
    print(int(n+1))