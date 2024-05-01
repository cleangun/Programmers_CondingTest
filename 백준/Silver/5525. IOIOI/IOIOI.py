import sys; input = sys.stdin.readline

n = int(input())
length = int(input())

line = input().rstrip()

ch_i = n+1; ch_o = n
result = 0

for j in range(length - (n*2)):
    ch = line[j]
    
    if ch == "I":
        isOk = False
        for i in range(1,ch_i+ch_o):
            # i 여야함
            if i % 2 == 0 and line[j+i] == "I":
                isOk = True
            # o 여야함    
            elif i % 2 == 1 and line[j+i] == "O":
                isOk = True
            else:
                isOk = False
                break
        if isOk:
            result += 1
print(result)
            

