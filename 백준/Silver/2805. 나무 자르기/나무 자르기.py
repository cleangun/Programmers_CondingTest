import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())

trees = [int(num) for num in input().rstrip().split()]
trees = sorted(trees, key=lambda x: -x)

# height = trees[0]
# jump = 10 ** (len(str(height)) - 1)

start = 0
end = trees[0] + 1
result = 0


# while jump > 0:
#     sum = 0
#     for tree in trees:
#         if tree <= height:
#             break
#         sum += tree - height
#     # print(f"height = {height}")
#     # print(f"sum = {sum}")
#     if sum >= m:
#         result = height
#         height += jump
#         jump = jump // 10
#         continue
#     else:
#         height -= jump

while start <= end:
    mid = (start + end) // 2
    total = 0

    for tree in trees:
        if tree <= mid:
            break
        total += tree - mid
    
    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)