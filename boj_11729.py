import sys

def hanoi(num, start, end, temp):
    if num == 1:
        print(start, end)
        return
    
    hanoi(num-1, start, temp, end)
    print(start, end)
    hanoi(num-1, temp, end, start)

n = int(sys.stdin.readline())

print(pow(2, n) - 1)
hanoi(n, 1, 3, 2)