import collections.abc as abc
import types
from dataclasses import dataclass

class Klass:
    
    클래스속성 ="Klass"
    
    def __init__(self, name):
        self.인스턴스속성 = name


@dataclass
class Person:
    name: str
    age: int 

@dataclass
class Product:
    name:str
    unit_price:float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
    
if __name__ == "__main__":
    # print(abc.Callable)

    # print(abc.Callable.__abstractmethods__)

    # print(isinstance(sum, abc.Callable))


    # print(issubclass(Klass, object))
    # print(issubclass(Klass, type))
    # print(isinstance(Klass, type))

    # print(isinstance(object, type))
    # print(isinstance(int, type))
    # print(isinstance(dict, type))

    # k = Klass("달")

    # print(type(k))
    # print(k.__class__)


    # # count = 0

    # # for i in dir(k):
    # #     print(i, end=', ')
    # #     count +=1

    # #     if count % 5 ==0:
    # #         print()


    # # print(Klass("z").__init__)

    # # print(type(Klass.__init__ )== types.FunctionType)
    # # print(type(k.__init__) == types.MethodType)

    # s11 = str("가을이가")

    # s22 = str(s11)

    # print(s11 is s22)

    # print(Person.__dict__['__init__'])

    # p = Person("moon", 52)
    # print(p.__dict__)

    # p.sex = "male"
    
    # print(p.__dict__)


    # i = Product("book", 1000.0, 10)

    # print(i.total_cost())


    # print(dir(k))

    #print(vars())



    # x = range(5)
    # it = iter(x)
    # issubclass(range, abc.Iterator)
    # print(issubclass(it, abc.Iterator))

    print(type(map))