'''
1. a, b가 주어졌을 때, b가 a보다 크면 b의 값을 a로, a의 값을 b로 지정한다.
2. a를 b로 나눈 나머지를 n으로 지정한다.
3. n이 0이면 b가 최대공약수이다. (종료)
4. n이 0이 아니라면, a의 값을 b로, b의 값을 n로 지정하고, 2번으로 돌아간다.
'''


def GCD(a, b):  # 두 정수를 받은 함수 지정
    if a < b:  # 무조건 왼쪽이 크게 배치
        a, b = b, a

    n = a % b

    if n == 0:  # 탈출조건
        return b
    else:
        return GCD(b, n)  # 정해진 조건대로 재귀
