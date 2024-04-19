graph = []
for i in range(8):
    line = list(input())
    graph.append(line)

result = 0
for y in range(len(graph)):
    isEven = True if y % 2 == 0 else False
    for x in range(len(graph[y])):
        if isEven:
            if (x % 2 == 0) and (graph[y][x] == "F"):
                result += 1
        else:
            if (x % 2 == 1) and (graph[y][x] == "F"):
                result += 1

print(result)

                


