# 10818 최소, 최대
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

print(min(li), max(li), end=' ')