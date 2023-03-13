import sys

n = int(sys.stdin.readline())

arr=[]
for i in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)

sorted_Arr = []

def select_Sort(s, length):
    if length == 1:
        num = s.pop(0)
        sorted_Arr.append(num)
        return
    num = min(s)
    for i in range(length):
        if s[i] == num:
            temp = s.pop(i)
            sorted_Arr.append(temp)
            select_Sort(s, length - 1)
            return

select_Sort(arr, n)
for i in range(n):
    print(sorted_Arr[i])