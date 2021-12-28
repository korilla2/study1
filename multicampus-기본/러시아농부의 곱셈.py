'''
왼쪽에 있는 수는 2로 나눠주고, 나머지는 버린다. (1이 될때까지 반복)
오른쪽에 있는 수는 두배를 해준다.
왼쪽에 있는 수가 홀수인 오른쪽의 수들을 모두 더해준다.

123 x 12
61 x 24
30 x 48
15 x 96
7 x 192
3 x 384
1 x 768
'''


# 문자열 분리 함수
def farmer(expression):  # 문자열 식을 그대로 받아옴
    result = []  # 마지막에 더해야 할 오른쪽 숫자 모아둘 빈 리스트
    expression = expression.split(' x ')  # 양 문자 분리
    left = int(expression[0])  # 왼쪽 숫자형으로 변경 후 변수에 담음
    right = int(expression[1])  # 오른쪽 숫자형으로 변경 후 변수에 담음
    recursion(left, right, result)  # 분리 다 했으니 본격적으로 연산을 위해 재귀함수로 보냄
    return sum(result)  # 얘는 가장 마지막 단계, 넘겨받은 리스트에 있는 모든 숫자 더해서 리턴


# 재귀 함수
def recursion(left, right, result):  # 왼쪽 오른쪽 그리고 빈리스트를 farmer 함수로부터 받아옴
    if left % 2 == 1:
        result.append(right)  # 왼쪽 숫자가 홀수라면, 오른쪽 숫자를 리스트에 담아둠
    if left < 2:
        return result  # 왼쪽 숫자 더이상 나눌 수 없다면 farmer 함수에게 모아둔 리스트를 전달해 줌
    return recursion(left//2, right*2, result)  # 숫자 규칙에 맞게 변화시키며 재귀


# 결과값들 비교 출력
print(123 * 12)
print(farmer('123 x 12'))
print('-'*20)
print(61 * 24)
print(farmer('61 x 24'))
print('-'*20)
print(30 * 48)
print(farmer('30 x 48'))
print('-'*20)
print(15 * 96)
print(farmer('15 x 96'))
print('-'*20)
print(7 * 192)
print(farmer('7 x 192'))
print('-'*20)
print(3 * 384)
print(farmer('3 x 384'))
print('-'*20)
print(1 * 768)
print(farmer('1 x 768'))
