from collections import deque
from datetime import datetime

a = []
ans = []
arg = list(input().split(" "))
arg[0] = int(arg[0])
arg[1] = int(arg[1])
for i in range(1, arg[0]+1):
    a.append(i)

length = arg[0]
moved = 0
while length > 0:
    moved += arg[1]-1
    if moved >= length:
        moved %= length
    temp = a.pop(moved)
    length -= 1
    ans.append(temp)

print("<", end="")
for i in range(arg[0]):
    if i == arg[0]-1:
        print(ans[i], end = ">")
    else:
        print(ans[i], end = ", ")
