import sys; input = sys.stdin.readline
n = int(input())

meet_lst = []

for _ in range(n):
    meet_lst.append(list(map(int,input().rstrip().split())))

meet_lst.sort(key=lambda x : (x[1], x[0]))

result = 0
pe = 0 # prev_end

for s,e in meet_lst:
    if s >= pe:
        result += 1
        pe = e
print(result)
