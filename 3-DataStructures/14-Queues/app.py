# FIFO = FIRST IN FIRST OUT
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()
print(queue)
if not queue:
    print("empty")
