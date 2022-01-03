'''
리스트만을 이용해서 덱을 구현해봅니다.
https://www.acmicpc.net/problem/10866
'''
import sys
input = sys.stdin.readline

n = int(input())
deck = []

for i in range(n):
    a = input().split()

    if a[0] == 'push_front':
        deck.insert(0, int(a[1]))

    elif a[0] == 'push_back':
        deck.append(int(a[1]))
    elif a[0] == 'pop_front':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])
            del deck[0]
    elif a[0] == 'pop_back':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[-1])
            deck.pop()
    elif a[0] == 'size':
        print(len(deck))

    elif a[0] == 'empty':
        if len(deck) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])
    elif a[0] == 'back':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[-1])
