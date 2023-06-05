# 15552 빠른 A+B
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(1, t+1):
    a, b = map(int, input().rstrip().split())
    sum = a+b
    print(sum)