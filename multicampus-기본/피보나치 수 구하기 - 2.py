'''
동일한 문제를 리스트를 이용하지 않고 변수 2개를 이용해서 구해 봅니다.
https://www.acmicpc.net/problem/2747
'''

n = int(input())  # 정수 하나를 입력받음


def recursion(n):  # 함수안에 정수가 들어감
    if n < 2:  # 피보나치는 3번째 밑은 구할 필요가 없으므로 최소조건으로 사용
        return n
    else:
        # 구하려는 항은 이전 항, 이전 이전항의 합으로 구해짐
        return recursion(n - 1) + recursion(n - 2)
