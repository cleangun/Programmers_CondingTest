from collections import deque

def solution(land):
    answer = []
    width = len(land[0])
    height = len(land)
    # x좌표에 따라 가치를 매기기 위한 list
    value_list = [0] * width
    
    visited = set()
    for y in range(height):
        for x in range(width):
            if land[y][x] == 1 and (y,x) not in visited:
                x_group = set()
                value = 0
                queue = deque([(y,x)])
                dx = [-1,1,0,0]
                dy = [0,0,-1,1]
                while queue:
                    current_y, current_x = queue.popleft()
                    visited.add((current_y, current_x))
                    # 가치 +1
                    value += 1
                    
                    # 해당 오일그룹에 x값에 가치를 매기기 위한 x좌표 모음
                    if current_x not in x_group:
                        x_group.add(current_x)
                    
                    for i in range(4):
                        target_x,target_y = current_x+dx[i], current_y + dy[i]
                        # land의 범위를 초과하지는 않는지
                        if (target_x >= width or target_x < 0) or (target_y >= height or target_y < 0):
                            continue
                        # 방문한 적이 없는, 값이 1인 위치라면
                        if ((target_y, target_x) not in visited) and (land[target_y][target_x] == 1):
                            queue.append((target_y, target_x))
                            visited.add((target_y,target_x))
                            
                # x그룹에 있는 x좌표마다 가치를 추가함
                for list_x in x_group:
                    value_list[list_x] += value
    return max(value_list)