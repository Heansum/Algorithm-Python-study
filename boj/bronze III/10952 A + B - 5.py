import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    if a == 0 & b == 0:
        break
    print(a + b)