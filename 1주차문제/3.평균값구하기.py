T = int(input())


for i in range(T):
    a = list(map(int, input().split()))
    print(f'#{i+1} {round(sum(a)/len(a))}')
