# 원형 큐 만들기
def is_empty_queue():
    global rear, front, queue, size
    if front == rear:
        return True
    return False


def is_full_queue():
    global rear, front, queue, size
    if (rear+1) % size == front:
        return True
    return False


def en_queue(data):
    global rear, front, queue, size
    if is_full_queue():
        return
    rear = (rear+1) % size
    queue[rear] = data
    return


def de_queue():
    global rear, front, queue, size
    if is_empty_queue():
        return
    front = (front+1) % size
    data = queue[front]
    queue[front] = None
    return data


# 메인 코드
T = int(input())


for i in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    # 기본 큐 생성
    size = len(a) + 1
    queue = [None for _ in range(size)]
    front = rear = 0

    # 큐에 넣어주기
    for j in a:
        en_queue(j)

    # 디큐와 인큐 M번만큼 반복
    for k in range(M):
        temp = de_queue()  # 디큐해서 나온 데이터를 보관
        en_queue(temp)  # 그대로 다시 인큐로 넣어줌
    result = (front+1) % size
    print(f'#{i+1} {queue[result]}')

# 런 타임 에러 발생
# 찾고싶은 값이 queue[front + 1] 이라면
# result = (front+1) % size
# queue[result] 이런식으로 바꿔서 사용해주자
