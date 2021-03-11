def solution():

    alpha_count = [0] * 26

    s = input()

    if len(s) > 100:
        return

    s_list = list(s)

    # 소문자 알바펫 돌면서 포함되어있는 지 확인
    # 있는 경우 알파벳의 인덱스 찾기
    # alpha_count에 인덱스 값 넣기

    for i in range(97, 123):
        if chr(i) in s:
            index = s_list.index(chr(i))
            alpha_count[i - 97] = index
        else:
            alpha_count[i - 97] = -1

    for value in alpha_count:
        print(value)
solution()



