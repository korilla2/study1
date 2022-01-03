'''
리스트만을 이용해서 큐를 구현해봅니다.
https://www.acmicpc.net/problem/10845
'''
import sys
input = sys.stdin.readline

n = int(input())
que = []

for i in range(n):
    a = input().split()

    if a[0] == 'push':
        que.append(int(a[1]))
    elif a[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif a[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
    elif a[0] == 'size':
        print(len(que))
    elif a[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
            del que[0]
