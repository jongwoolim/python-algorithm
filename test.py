import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(collections.Counter(participant))
    print(collections.Counter(completion))
    # print(answer)
    # print(list(answer.keys()))
    return list(answer.keys())[0]


participant = ["leo", "jongwoo","dongwoo"]
completion = ["jongwoo", "dongwoo"]
result = solution(participant, completion)

print(result)


def solution(phone_book):
    phone_book.sort( reverse=True)
    print(phone_book)
    l = tuple(phone_book)
    for i in range(len(phone_book) - 1):
        k = phone_book[i]
        if k.startswith(l[i + 1:]):
            return False

    return True

#phone_book = ['123', '456', '789']
phone_book = ['119', '97674223', '1195524421']
print(solution(phone_book))

