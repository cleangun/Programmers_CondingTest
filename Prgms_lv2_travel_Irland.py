# 프로그래머스 - 무인도 여행 (level 2)
from collections import deque

maps = ["X591X", "X1X5X", "X231X", "1XXX1"]


def bfs(maps, arr, sum):
  visit = deque([arr])
  while visit:
    x, y = visit.popleft()
    if maps[y][x] == 'X':
      continue

    sum += int(maps[y][x])
    maps[y][x] = 'X'
    if (x + 1) < len(maps[0]):
      if maps[y][x + 1] != 'X':
        visit.append([x + 1, y])
    if x - 1 >= 0:
      if maps[y][x - 1] != 'X':
        visit.append([x - 1, y])
    if y + 1 < len(maps):
      if maps[y + 1][x] != 'X':
        visit.append([x, y + 1])
    if y - 1 >= 0:
      if maps[y - 1][x] != 'X':
        visit.append([x, y - 1])
  return sum


def solution(maps):
  maps = [list(map(str, i)) for i in maps]
  answer = []
  for y in range(len(maps)):
    for x in range(len(maps[y])):
      if maps[y][x] == 'X':
        continue
      else:
        answer.append(bfs(maps, [x, y], 0))
  answer.sort()
  return answer if answer else [-1]


print(solution(maps))
