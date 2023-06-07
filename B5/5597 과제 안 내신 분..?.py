# 5597 과제 안 내신 분..?
import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(28)]

for i in range(1, 31):
    if i not in nums:
        print(i)