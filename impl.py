
#--------
x, y = 1,1

n = int(input())

plans = input().split()
#동,서,남,북
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']


for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
        #공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
    x, y = nx, ny

print(x, y)


#-------시간 문제
h = int(input())

count = 0 

for i in range(h+1):
    for j in range(60):
        for k in range(60):

            #매 시간 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)


#---------왕실 나이트 구현 문제

#현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

#나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0

for step in steps:

    #이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    #해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
        
print(result)


#--------문자열 재정렬

data = input()
result = []
value = 0

#문자를 하나씩 확인한다
for x in data:
    #알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    #숫자는 따로 더하기
    else:
        value += int(x)

#알파벳을 오름차순으로 정렬
result.sort()

#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

#최종 결과 출력
print(''.join(result))



    
        
