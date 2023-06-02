# 2438 별 찍기 - 1
import sys
input = sys.stdin.readline

n = int(input())
star = str()

for i in range(1, n+1):
    star += '*'
    print(star)