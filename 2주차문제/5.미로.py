from collections import deque

end = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def find_end(arr, i, j):

    stack = deque()
    start = arr[i][j]
    stack.append((i, j))
    while stack:
        i, j = stack.pop()

        for i in range(4):
            ni = i + di[i]
            nj = j + dj[i]

            if ni < 0 or ni >= len(arr) or nj < 0 or nj >= len(arr):
                continue
            if arr[ni][nj] == 1:
                continue
            if arr[ni][nj] == 0:
                arr[ni][nj] = 1
                stack.append((ni, nj))
            if arr[ni][nj] == 2:
                return 1
    return 0


def find_start(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 3:
                find_end(arr, i, j)


for j in range(end):
    T = int(input())
    arr = []
    for i in range(T):
        arr.append(list(map(int, input())))
    print(arr)
    print(find_start(arr))
https: // swexpertacademy.com/main/learn/course/lectureProblemViewer.do
