T = int(input())

for i in range(T):
    N = int(input())
    N_list = [num for num in range(1, N+1)]
    result = []
    for j in N_list:
        if j % 2 == 0:
            result.append(-j)
        else:
            result.append(j)
    print(f'#{i+1} {sum(result)}')
