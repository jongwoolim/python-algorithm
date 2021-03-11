from bisect import bisect_left, bisect_right

def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)
    
#n(원소의 개수)과 target(찾고자 하는 값)

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
    

#값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]

print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))

#------떡볶이 떡 만들기

#떡의 개수(N)와 요청한 떡의 길이(M)을 입력
n, m = map(int, input().split())

#각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

#이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

#이진 탐색
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        #잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid

        #떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
        if total < m:
            end = mid - 1
        #떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
        else:   
            result = mid
            start = mid + 1
print(result)




