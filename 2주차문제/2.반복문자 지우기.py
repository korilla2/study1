# 스택 함수들 만들기

def is_empty_stack():
    global size, top, stack
    if top == -1:
        return True
    return False


def is_full_stack():
    global size, top, stack
    if top == size - 1:
        return True
    return False


def push_stack(data):
    global size, top, stack
    if is_full_stack():
        return
    top += 1
    stack[top] = data
    return


def pop_stack():
    global size, top, stack
    if is_empty_stack():
        return
    stack[top] = None
    top -= 1
    return


# 메인코드
T = int(input())

# 기본 스택 잡아주기
for i in range(T):
    a = list(input())
    size = len(a)
    stack = [None for _ in range(size)]
    top = -1

    # 스택 안에 문자를 넣으면서 같은 문자 만나면 둘 다 제거
    for j in a:
        temp = stack[top]
        push_stack(j)
        if stack[top] == temp:
            pop_stack()
            pop_stack()

    # 스택에 남은 문자 갯수 세어주기
    cnt = 0
    for k in stack:
        if k == None:
            continue
        else:
            cnt += 1
    print(f'#{i+1} {cnt}')
