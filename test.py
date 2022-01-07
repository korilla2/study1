def make_tree(n):
    global cnt
    if n <= 6:
        make_tree(n*2)

        arr[n] = cnt
        cnt += 1

        make_tree(n*2 + 1)


arr = [None for _ in range(7)]
cnt = 1
make_tree(1)
print(arr)
