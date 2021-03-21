import sys
import heapq

# input = sys.stdin.readline
#----수 정렬하기2
# def heapsort(iterable):
#     h = []
#     result = []
#
#     # 모든 원소를 차례대로 힙에 삽입 ,, 삽입 제거시 -부호를 붙이면 max-Heap
#     for value in iterable:
#         heapq.heappush(h, value)
#         # heapq.heappush(h, -value) 최대 힙 입력
#
#     # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
#     for i in range(len(h)):
#         result.append(heapq.heappop(h))
#         # result.append(-heapq.heappop(h)) 최대 힙 꺼내기
#
#     return result
#
# n = int(input())
# inputs = []
# for _ in range(n):
#     m = int(input())
#     inputs.append(m)
# result = heapsort(inputs)
#
# for v in result:
#     print(v)

#---- 수 정렬하기3
# import sys
# input = sys.stdin.readline
# m=10001;l=[0]*m
# for _ in range(int(input())):l[int(input())]+=1
# for i in range(1,m):print(f"{i}\n"*l[i],end="")
#---- 수 정렬하기4
# num_list = list(map(int, input()))
# num_list.sort(reverse=True)
# print(''.join(str(v) for v in num_list))

#---- 좌표 정렬하기
n = int(input())

arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort(key=lambda v: (v[0], v[1]))

for x, y in arr:
    print(x,y)






