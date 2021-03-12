import sys
def solution():

    n = int(sys.stdin.readline())
    arr = []

    for _ in range(n):
        num = int(input())
        arr.append(num)

    arr.sort()

    for v in arr:
        print(v)
solution()