import sys; input = sys.stdin.readline
n = int(input())

graph = []
for _ in range(n):
    graph.append([int(ch) for ch in input().rstrip().split()])

def rect(x,y,length, white, blue):
    # 길이를 더 나눌 수 없으면 sum return
    if length == 1:
        if graph[y][x] == 1:
            return white, blue+1
        return white+1, blue  # else

    # 다 칠해져 있는지 확인 => 칠해져있으면 return (1개)
    whiteCnt , blueCnt = 0, 0
    for yi in range(y, y+length):
        for xi in range(x, x+length):
            if graph[yi][xi] == 1:
                blueCnt += 1
            else: whiteCnt += 1
    
    if whiteCnt == length**2:
        return white+1, blue
    elif blueCnt == length**2:
        return white, blue+1

    # 아니면 4개로 쪼개기
    white,blue = rect(x,y, length//2, white, blue)
    white,blue = rect(x + (length//2), y, length//2, white, blue)
    white,blue = rect(x,y + (length//2), length//2, white, blue)
    white,blue = rect(x + (length//2), y + (length//2), length//2, white, blue)

    return white,blue
    

white,blue = rect(0,0,n,0,0)
print(white)
print(blue)