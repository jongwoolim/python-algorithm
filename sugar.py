a = int(input())
b = int(input())

arr1 = []
arr2 = []
temp = [] #중간 연산 결과
result = []
idx = 0
#입력받은 수 arr1배열에 넣기
for _ in range(3):
    arr1.append(a % 10)
    a //= 10

#입력받은 수 arr2배열에 넣기
for _ in range(3):
    arr2.append(b % 10)
    b //= 10

for i in arr2:
    
    share = 0 # 몫
    for j in arr1:
        temp.append((j * i)%10 + share)
        share = (j * i //10)
        if j == arr1[len(arr1)-1]:
            temp.append(share)

    temp.reverse()
    print(temp)
    cList = temp[:]

    if(idx == 1):
        cList.append(0)
        result.append(cList)
    elif(idx == 2):
        for _ in range(idx):
            cList.append(0)
        result.append(cList)
    else: result.append(cList)
    temp.clear()
    idx = idx + 1

sList = []
for i in range(len(result)):
    sList.append(str(result[i]))


# print(arr1)
# print(arr2)
print(result)
print(sList)