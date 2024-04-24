n = int(input())

meet_lst = []

for _ in range(n):
    s,e = map(int,input().split())
    meet_lst.append([s,e])

meet_lst.sort(key=lambda x : (x[1], x[0]))


result = 0
pe = 0 # prev_end

for s,e in meet_lst:
    if s >= pe:
        result += 1
        pe = e

print(result)
