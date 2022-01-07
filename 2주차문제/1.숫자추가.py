# 노드 클래스와 함수 만들기
class Node():
    def __init__(self):
        self.data = None
        self.next = None


def insert_node(idx, data):
    global pre, head, current
    if idx == 0:
        node = Node()
        node.data = data
        node.next = head
        head = node
        return
    else:
        current = head
        for i in range(idx-1):
            current = current.next
        node = Node()
        node.data = data
        node.next = current.next
        current.next = node
        return


def print_node(L):
    global pre, head, current
    current = head
    # print(current.data, end=' ')
    for i in range(L):
        current = current.next
    return current.data


# 전역 변수
pre, current, head = None, None, None


# 메인 코드
T = int(input())

for k in range(T):
    N, M, L = map(int, input().split())

    arr = list(map(int, input().split()))

    # 헤드 먼저 만들기
    node = Node()
    node.data = arr[0]
    head = node

    # 나머지 부분도 노드로 만들어 연결
    for i in arr[1:]:
        pre = node
        node = Node()
        node.data = i
        pre.next = node

    # 삽입 연산 수행
    for i in range(M):
        a = list(map(int, input().split()))
        insert_node(a[0], a[1])
    print(f'#{k+1} {print_node(L)}')
