from collections import deque

dx_list = [-1, 1, 0, 0]
dy_list = [0, 0, -1, 1]


def find_start(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                result = find_end(arr, i, j)
    if result == 3:
        return 1
    else:
        return 0


def find_end(arr, i, j):
    queue = deque()
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx = x + dx_list[i]
            dy = y + dy_list[i]

            if dx < 0 or dy < 0 or dx > len(arr) - 1 or dy > len(arr) - 1:
                continue
            elif arr[dx][dy] == 1:
                continue
            elif arr[dx][dy] == 3:
                while len(queue) > 0:
                    queue.popleft()
                break
            elif arr[dx][dy] == 0:
                arr[dx][dy] = 1
                queue.append((dx, dy))
    if dx < 0 or dy < 0 or dx > len(arr) - 1 or dy > len(arr) - 1:
        return False
    return arr[dx][dy]


T = int(input())


for i in range(T):
    N = int(input())
    arr = []
    for j in range(N):
        arr.append(list(map(int, input())))
    print(f'#{i+1} {find_start(arr)}')
