'''
스택의 동작 과정을 이해해봅시다.
- 리스트만 이용해서 구현
https://www.acmicpc.net/problem/10828
'''
import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):

    a = list(input().split())
    if a[0] == 'push':
        stack.append(int(a[1]))

    elif a[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
