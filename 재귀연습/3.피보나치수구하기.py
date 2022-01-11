# https://www.acmicpc.net/problem/2747
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n = int(input())


def recursion(n):
    if n < 2:
        return n
    else:
        return recursion(n - 1) + recursion(n - 2)


print(recursion(n))
