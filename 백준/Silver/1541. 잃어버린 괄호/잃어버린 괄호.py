import sys; input = sys.stdin.readline
numlist, oplist = [], []

exp = input().rstrip()

string_num = ""
for ch in exp:
    if ch.isdigit():
        string_num += ch
    else:
        numlist.append(int(string_num))
        string_num = ""
        oplist.append(ch)
if string_num != "":
    numlist.append(int(string_num))

if "-" in oplist:
    minus_index = oplist.index("-")
    print(sum(numlist[:minus_index+1]) - sum(numlist[minus_index+1:]))
else:
    print(sum(numlist))