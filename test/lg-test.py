def solution1(teamIDs, additional):

    answer = []

    for add_item in additional:
        print(add_item)
        for team in teamIDs:

            print("team ", team)
            if add_item == team:
                print("find", add_item)
                break
        if add_item != team:
            answer.append(add_item)
            teamIDs.append(add_item)

    print(answer)


# teamIDs = ['world', 'prog']
# additional = ['hello', 'world', 'code', 'hello', 'try', 'code']
teamIDs = ['abc', 'hq','xyz']
additional = ['hq', 'abc', 'pp', 'xy', 'pp', 'hq']
solution1(teamIDs, additional)



def solution2(p, n):

    answer = ""
    h = p[3:5]
    m = p[6:8]
    s = p[9:11]
    round_num = 0
    # print(type(h))
    print(h, m, s)

    if p[:2] == 'PM':

        #초 단위 덧셈
        #결과가 10이하인 경우 '0'붙히기 60이상이면 '00' 셋팅하고 올림 숫자
        #분도 반복
        #시간은 <12 이면 + 12, >= 12 이면 00

        add_s = int(s) + n
        if add_s < 10:
            s = '0' + str(add_s)

            if int(h) < 12:
                h = str(int(h) + 12)

        elif add_s >= 60:
            round_num = (int(s) + n) - 60
            s = '00'

            if round_num == 0:
                add_m = int(m) + round_num + 1
            else:
                add_m = int(m) + round_num

            if add_m <= 10:
                m = '0' + str(add_m)

                if int(h) < 12:

                    h = str(int(h) + 12)
                # else:
                #     if h // 12 < 12:
                #         h = '0' + str(h // 12)
                #     # else:
                #     #     h = str(h // 12)

            elif add_m >= 60:
                m = '00'

                h = str(int(h) + 1)
                if int(h) < 12:

                    h = str(int(h) + 12)

                else:
                    h = '00'

        else:
            s = str(add_s)

            if int(h) < 12:
                h = str(int(h) + 12)




    answer = h +':' + m +':' + s
    return answer


print(solution2("PM 11:59:59", 10))
