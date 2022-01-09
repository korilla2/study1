from collections import deque

queue = deque()

queue.append('A')
queue.popleft()
queue.append('B')
queue.append('C')
queue.popleft()
queue.append('D')
queue.popleft()
queue.append('E')
queue.append('F')
queue.popleft()
queue.append('G')
queue.popleft()
queue.append('H')

print(queue)
