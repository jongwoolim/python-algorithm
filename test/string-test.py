#----알파벳 찾기
# def solution():
#
#     alpha_count = [0] * 26
#
#     s = input()
#
#     if len(s) > 100:
#         return
#
#     s_list = list(s)
#
#     # 소문자 알바펫 돌면서 포함되어있는 지 확인
#     # 있는 경우 알파벳의 인덱스 찾기
#     # alpha_count에 인덱스 값 넣기
#
#     for i in range(97, 123):
#         if chr(i) in s:
#             index = s_list.index(chr(i))
#             alpha_count[i - 97] = index
#         else:
#             alpha_count[i - 97] = -1
#
#     for value in alpha_count:
#         print(value)


#----문자열 반복
# def solution():
#
#     case = int(input())
#     result = ""
#
#     for _ in range(case):
#         r, s = input().split()
#
#         if len(s) <1 or len(s) > 20:
#             return
#
#         num = int(r)
#
#         for value in s:
#             for _ in range(num):
#                 result += value
#         result += " "
#     result_arr = result.split()
#
#     for value in result_arr:
#         print(value)

#----단어공부
# def solution():
#
#     alpha_count = [0] * 123
#     max_count = 0
#     inputs = input().lower()
#
#     for value in inputs:
#         alpha_count[ord(value)] += 1
#
#     for i in range(97, 123):
#         if max(alpha_count) == alpha_count[i]:
#             max_count += 1
#
#     if max_count > 1:
#         print('?')
#         return
#     else:
#         print(chr(alpha_count.index(max(alpha_count))).upper())

#----단어 개수
# def solution():
#
#     s = input().split()
#     result = 0
#     for _ in s:
#         result += 1
#     print(result)

#----상수
# def solution():
#
#     a, b = input().split()
#
#     a_reverse = int(a[::-1])
#     b_reverse = int(b[::-1])
#
#     if a_reverse > b_reverse:
#         return print(a_reverse)
#     else:
#         return print(b_reverse)

#----다이얼
# def solution():
#
#     time_arr = [0] * 10
#     alpha_dict = {1: '0', 2 : 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7 : 'PQRS', 8: 'TUV', 9: 'WXYZ', 10: '9'}
#
#     result = 0
#
#     for i in range(2, len(time_arr)+2):
#         time_arr[i-2] = i
#
#     print(time_arr)
#     s = input().upper()
#
#     if len(s) < 2 or len(s) > 15:
#         return
#
#     for alpha in s:
#         for key, value in alpha_dict.items():
#             if alpha in value:
#                 result += time_arr[key - 1]
#     print(result)

#---- 크로아티아 알파벳
# def solution():
#     arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#
#     alpha = input()
#     for v in arr:
#         alpha = alpha.replace(v, '*')
#     print(len(alpha))

# def solution():
#
#     n = int(input())
#     count = 0
#     if n < 1 or n > 100:
#         return
#
#     for _ in range(n):
#         word = list(input().lower().split())
#
#         while len(word) > 0:
#             s = word.pop()

#---- 그룹 단어 체
def solution():
# ccazzzbb는 c,a,z,b 모두 연속해서 나타나서 그룹 단어
# aabbbccb는 b가 떨어져서 그룹 단어가 아니다
# a~z 리스트 만든다
# 문자열을 하나씩 돌면서 카운트한다
# 해당 문자열이 전 문자열과 같으면 카운트, 같지 않고  알파벳 카운트가 0이상이그룹단어 x
    n = int(input())
    words = []
    alpha_count = [0] * 26
    result = 0

    for _ in range(n):
        word = input()
        words.append(word)

    for w in words:
        group_checked = True
        for i in range(len(w)):
            if i > 0:
                if w[i] == w[i - 1]:
                    alpha_count[ord(w[i]) - 97] += 1
                else:
                    if alpha_count[ord(w[i]) - 97] > 0:
                        group_checked = False
                        break

            alpha_count[ord(w[i]) - 97] += 1

        if group_checked:
            result += 1
        # alpha_count.clear()
        del alpha_count[:]
        alpha_count = [0] * 26
    print(result)

solution()


