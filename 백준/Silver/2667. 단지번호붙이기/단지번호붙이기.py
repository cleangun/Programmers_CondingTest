import sys; from collections import deque
input = sys.stdin.readline
result = []; visited = set()
graph = []

def bfs(y,x):
    global visited

    cnt = 0
    queue = deque([(y,x)])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        y,x = queue.popleft()
        visited.add((y,x))
        cnt += 1
        for i in range(4):
            ny,nx = y + dy[i], x + dx[i]
            if (0 > ny or ny >= len(graph)) or (0 > nx or nx >= len(graph[0])):
                continue
            if graph[ny][nx] == 1 and (ny,nx) not in visited:
                visited.add((ny,nx))
                queue.append((ny,nx))
    return cnt

n = int(input())

for _ in range(n):
    line = [ int(num) for num in input().rstrip()]
    graph.append(line)

for y in range(len(graph)):
    for x in range(len(graph[0])):
        if (y,x) not in visited and graph[y][x] == 1:
            result.append(bfs(y,x))

print(len(result))
for i in sorted(result):
    print(i)