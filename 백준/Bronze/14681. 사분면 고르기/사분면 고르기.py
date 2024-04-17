x = int(input())
y = int(input())

if x < 0:
    print(2 if y > 0 else 3)
else:
    print(1 if y > 0 else 4)