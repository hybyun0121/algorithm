import math
import sys

num = int(input())
pi = list(map(int, input().split()))

def solution(num, pi):
    pi = sorted(pi)
    tmp = 0
    answer = 0
    for i in pi:
        i = int(i)
        tmp += i
        answer += tmp
    return answer

print(solution(num, pi))
