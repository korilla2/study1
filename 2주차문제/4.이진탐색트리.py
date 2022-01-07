class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def make_tree(n):
    global N, cnt
    if n <= N:
        make_tree(n*2)

        a[n] = cnt
        cnt += 1

        make_tree(n*2 + 1)


T = int(input())

for i in range(T):
    N = int(input())
    a = [None for _ in range(N+1)]
    cnt = 1
    make_tree(1)

    print(f'#{i+1} {a[1]} {a[N//2]}')
