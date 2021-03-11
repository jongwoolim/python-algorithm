# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n, s = map(int, input().split())

if s < 1 or s >=n:
	quit()
	
array = list(map(int, input().split()))


for i in range(s):
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1, n):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

result = list(map(str, array))
print(''.join(result))





