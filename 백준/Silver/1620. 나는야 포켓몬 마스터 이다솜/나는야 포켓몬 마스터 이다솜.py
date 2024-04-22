import sys; input = sys.stdin.readline
n, m = map(int, input().split())

dg = {};seq = 0
for _ in range(n):
    name = input().rstrip()
    seq += 1
    dg[name] = seq
    dg[str(seq)] = name

for _ in range(m):
    print(dg[input().rstrip()])
