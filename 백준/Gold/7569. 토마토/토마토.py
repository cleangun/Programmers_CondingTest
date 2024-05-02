import sys
from collections import deque
input = sys.stdin.readline
m,n,h = map(int,input().rstrip().split())

# 3차원 배열 (높이, y, x값 순)
graph = []
clear_height = []
result = 0
for _ in range(h):
    # 2차원 배열을 입력받아서 append해줌
    line = []
    for _ in range(n):
        line.append([int(num) for num in input().rstrip().split()])
    graph.append(line)

zero_cnt = 0 # 큐에 처음 1의 좌표를 담을때, 0의 갯수도 세어두면
            # 나중에 queue에 데이터가 안들어갔는데도 zero_cnt가 0이 안되면
            # 더 이상 바꿀 수 없는 것임 => -1 출력
queue = deque([])
# 초기 1의 위치 학인
for z in range(len(graph)):
    for y in range(len(graph[0])):
        for x in range(len(graph[0][0])):
            if graph[z][y][x] == 0:
                zero_cnt += 1
            elif graph[z][y][x] == 1:
                queue.append((z,y,x,0))
# 앞 , 뒤 , 왼, 오, 위, 아래
dz = [0,0,0,0,1,-1]
dx = [0,0,-1,1,0,0]
dy = [1,-1,0,0,0,0]

while queue:
    z,y,x,day = queue.popleft()
    if day > result: result = day

    for i in range(6):
        nz,nx,ny = z+dz[i], x+dx[i], y+dy[i]
        if (0 <= nz and nz < h) and (0 <= ny and ny < n) and \
            (0 <= nx and nx < m) and (graph[nz][ny][nx] == 0):
            graph[nz][ny][nx] = 1
            zero_cnt -= 1
            queue.append((nz,ny,nx,day + 1))
if zero_cnt > 0:
    result = -1

# print("-------final-------")
# for z in range(len(graph)):
#     for y in range(len(graph[0])):
#         print(graph[z][y])
# print(f"result : {result}")
# print(f"zero cnt : {zero_cnt}")
print(result)