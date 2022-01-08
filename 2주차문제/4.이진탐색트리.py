def make_tree(idx):
    global N, val, result
    if idx <= N:
        make_tree(idx * 2)

        result[idx] = val
        val += 1

        make_tree(idx * 2 + 1)


T = int(input())

for i in range(T):
    N = int(input())
    result = [None for _ in range(N+1)]

    idx = 1
    val = 1
    make_tree(idx)
    print(f'#{i+1} {result[1]} {result[N//2]}')
