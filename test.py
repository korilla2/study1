# 저는 이거부터 어렵네요..
t = int(input())

for test in range(1, t+1):
    n = map(int, input().split())
    sum = 0
    for i in n:
        if i % 2 != 0:
            sum += i
    print("#", str(test), str(sum))
