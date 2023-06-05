# 10807 개수 세기
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
v = int(input())

cnt = 0
for i in range(n):
    if v == li[i]:
        cnt += 1
print(cnt)