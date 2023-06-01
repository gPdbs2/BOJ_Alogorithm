# 25304 영수증
import sys
input = sys.stdin.readline

x = int(input())
n = int(input())
total = 0

for _ in range(1, n+1):
    a, b = map(int, input().split())
    price = a * b
    total += price

if x == total:
    print('Yes')
else:
    print('No')