# 2439 별 찍기 - 2
import sys
input = sys.stdin.readline

n = int(input())
gap = str()
star = str()

for i in range(1, n+1):
    gap = ' ' * (n-i)
    star += '*'

    print(gap + star)