# -*- coding: utf-8 -*-
'''
クラスでのデータと関数のテスト
'''
class MyClass:
    "A simple example class"
    def __init__(self):
        pass
    i = 12345
    '''
    pylintで、counterを関数外で定義しているエラーになるのは、
    ここで定義すればでなくなる。
　　ただ、外部で定義しても動くためのテストなので、そのままにする
    counter = 0
    '''

    def fun(self):
        "simple function"
        if self.i > 0:
            return 'hello world'


MYCLASS = MyClass()

MYCLASS.counter = 1
while MYCLASS.counter < 10:
    MYCLASS.counter = MYCLASS.counter * 2
print MYCLASS.counter
del MYCLASS.counter


class MyClass2:
    "A simple example class"
    def __init__(self):
        pass

    i = 12345
    '''
    selfをとったらエラーになった。クラス内の関数だから引数いるのかな.
    普通の関数定義なら、引数なくても動く
    '''
    def fun(self):
        "simple function with data"
        return 'hello world' + str(self.i)

YYY = MyClass2()
print YYY.fun()
