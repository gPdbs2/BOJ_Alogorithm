# 2562 최댓값
import sys
input= sys.stdin.readline

num = [0]+[int(input()) for _ in range(1, 10)]

print(max(num), num.index(max(num)), end='\n')