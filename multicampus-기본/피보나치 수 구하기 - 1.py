'''
https://www.acmicpc.net/problem/2747
'''
n = int(input())  # 몇 번째 인지 정수로 받아옴

a = 1  # 첫 번째 수는 고정
b = 1  # 두 번째 수도 고정
result = 0  # 결과를 위한 변수
for i in range(n - 2):  # 처음 두 개는 고정이므로 나머지만 반복
    result = a + b  # 1번 2번 수를 더해서 3번수로 만들어 주고
    a = b  # 1번수를 2번으로
    b = result  # 2번수를 3번으로 한칸씩 이동 후 반복

print(result)
