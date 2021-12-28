'''
n이 주어졌을 때, 2^n을 구하는 함수를 작성하세요
함수의 리턴값은 2^n한 결과 입니다.
'''


def power(n):  # n을 받는 함수
    a = 2  # 2의 거듭제곱 꼴이므로 2로 사용할 변수
    result = 1  # 최종 답이 될 변수
    for i in range(n):  # n번 반복
        result = result * 2  # 2씩 곱한값으로 계속 업데이트
    return result
