import sys;  input = sys.stdin.readline
from collections import deque
n, m = map(int,input().rstrip().split())
MAX = 10 ** 5
graph = [0] * (MAX + 1)

if n >= m:
    print(n-m)
    exit(0)

queue = deque([n])
while queue:
    x = queue.popleft()

    if x == m:
        print(graph[x])
        break
    for nx in [ x - 1, x + 1, x * 2]:
        if 0 <= nx <= MAX and not graph[nx]:
            graph[nx] = graph[x] + 1
            queue.append(nx)

    

        