import sys; import re;
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    command = input().rstrip()
    length = int(input())
    lst = [num for num in re.sub(","," ",re.sub("[ \[\] ]","",input().rstrip())).split()]
    
    # false => 기본, true => 반대
    isReverse = False
    isError = False
    frontidx , backidx = 0, len(lst)

    for ch in command:
        if ch == "R":
            isReverse = not isReverse
        if ch == "D":
            # 예외처리
            if (backidx - frontidx) < 1:
                isError = True
                break
            
            if isReverse == True:
                backidx -= 1
            else:
                frontidx += 1
    
    # 예외처리
    if isError:
        print("error")
        continue

    if isReverse == True:
        lst = list(reversed(lst[frontidx:backidx]))
        print("[" + ",".join(lst) + "]")
    else:
        print("[" + ",".join(lst[frontidx:backidx]) + "]")