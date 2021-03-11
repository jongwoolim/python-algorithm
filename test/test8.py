#----알파벳 찾
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


#----문자열 반
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
def solution():

    a, b = input().split()

    a_reverse = int(a[::-1])
    b_reverse = int(b[::-1])

    if a_reverse > b_reverse:
        return print(a_reverse)
    else:
        return print(b_reverse)

solution()



