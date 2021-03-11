import keyword
import string
import random
import math
import collections.abc as cols
import itertools as it
import operator as op

class Klass:

    def __init__(self, name):
        self.name = name


def index(iterable, *args):
    result = []

    for i in args:
        if i < len(iterable):

            result.append(iterable[i])
        else: continue

    return result

def func(x, y):
    return x, y

def high_order(func, *args):

    return func(*args)


if __name__ == "__main__":

    lotto = [x for x in range(1, 46)]

    random.shuffle(lotto)

    #print(random.choice(lotto))

    #print(type(Klass("jongwoo")))

    # print(globals()['Klass'])

    # k = Klass("jongwoo")
    # print(k.__dict__)
    # print(k.name)

    # x, *y = 1, 2,3

    # print(x, " ",y)
    # x,y = y,x
    # print(x, " ",y)

    # _list = [1,2,3,4,5]

    # m = map(math.sqrt, _list)

    # # ___list = [x for x in m] 

    # # print(___list)

    # # print(type(m))
    # # __list = [*m]
    # # print(type(__list))

    # l = [1,2,3,4]
    # ll = [5,6,7,8,9]

    # for i, v in enumerate(l):
    #     print("index " ,i, "value ", v)

    # for i in zip(l ,ll):
    #     print(i)

    # for i in it.zip_longest(l, ll):
    #     print(i)

    # for i in it.chain(l ,ll):
    #     print(i)

    # for i in it.combinations(l, 3):
    #     print(i)

    # count = 0

    # for i in it.permutations(l):

    #     print(i)
    #     count += 1
    #     if(count % 5 ==0):
    #         print()


    x = 5
    print("x는 10보다 작습니다") if x<10 else print("x는 10보다 큽니다")                

    def fun10():
        print(10)

    def fun20():
        print(20)


    switch = {'10': fun10, '20': fun20}

    print(globals()['switch'])

    switch.get('100', fun10)()

    ll = [1,2,3,4,5,6]

    #print(index(ll, 1,2,5))

    print(type(op.itemgetter))

    idx = op.itemgetter(1,2,5)

    print(idx(ll))




    value = high_order(func, 1,3)

    print(value)