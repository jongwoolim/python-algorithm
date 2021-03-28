def solution1(A):
    count = 0
    count_arr = []
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            if A[i] == 1:
                A[i+1] = 0
            elif A[i] == 0:
                A[i + 1] = 1
            count += 1
    count_arr.append(count)
    count = 0

    for i in range(len(A)-1):
        if A[i] == 0:
            A[i] = 1
        elif A[i] == 1:
            A[i] = 0

        if A[i] == A[i+1]:
            if A[i] == 1:
                A[i+1] = 0
            elif A[i] == 0:
                A[i + 1] = 1
            count += 1
    count_arr.append(count)

    print(min(count_arr))

# solution1([0,1,1,0])

def solution2(N):

    arr = []
    result = []
    str_num = str(N)
    minus_oper = False

    for i in range(len(str_num)):
        arr.append(str_num[i])

    if '-' in arr:
        minus_oper = True

    print(arr)
    print(minus_oper)


    if minus_oper:
        del arr[0]
        for i in range(len(arr)):
            arr.insert(i, '5')

            result.append(int('-'+''.join(arr)))
            del arr[i]
        print(max(result))
    else:
        for i in range(len(arr)):
            arr.insert(i, '5')
            result.append(int(''.join(arr)))
            del arr[i]
        print(max(result))

# solution2(-999)

def solution3(A, B):
    A_sum1 = 0
    A_sum2 = 0
    B_sum1 = 0
    B_sum2 = 0
    index_arr = []
    for i in range(len(A)):
        for j in range(0, i+1):
            A_sum1 += A[j]
            B_sum1 += B[j]

            for k in range(i + 1, len(A)):
                A_sum2 += A[k]
                B_sum2 += B[k]

        print('a_sum1',A_sum1)
        print('a_sum2',A_sum2)
        print('b_sum1',B_sum1)
        print('b_sum2',B_sum2)
        if A_sum1 == A_sum2 and B_sum1 == B_sum2:
            index_arr.append(i+1)
        print(index_arr)
    print(len(index_arr))
solution3([0,4,-1,0,3], [0,-2,5,0,3])