import os
import myFun
from app import *


def my_power(x,n):
    s=1
    while n>0:
        n = n-1
        s = s*x
    return s

if __name__=="__main__":
    print("hello world.")
    print("this second line.")
    print(len('中文'))
    print(len('abc'))
    str = 'this others setting.'
    print(str)
    classmates = ('Michael','Bob','Tray')
    print(classmates)
    ##tuple
    tpl = ('a', 'b', ['A', 'B'])
    print(tpl)
    age = 17
    if age>=18:
        print('your age is ',age)
        print('adult')
    elif age>=6:
        print('teenager')
    else:
        print('your age is ',age)
        print('kid')

    for cl in classmates:
        print(cl)
    ab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum =0
    for x in range(101):
        sum=sum+x
    print(sum)
    # dict its like map
    dit = {'Michael':98,'Bob':75,'Tracy':99}
    print('dict test:',dit['Michael'])
    print('dict get value:',dit.get('Bob'))
    dit.pop('Bob')
    print('after pop:',dit)
    # set test and learn
    st = set([1, 1, 2, 2, 3, 3])
    print('print set=',st)
    st.add(5)
    print('print set=',st)
    # function invoke
    print(myFun.my_abs(-99))
    print(my_power(9,8))
    myFun.enroll('Sarah', 'F')
    print(myFun.calc((1, 3, 5, 7)))
    print(myFun.calc2(2,3))
    print(myFun.person('Michael', 30))
    print(myFun.person('Bob', 35, city='Beijing'))
    print(myFun.person('Adam', 45, gender='M', job='Engineer'))
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    print(myFun.person('Jack', 24, **extra))
    print(myFun.person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))
    myFun.f1(1, 2, c=3)
    args = (1, 2, 3, 4)
    kw = {'d': 99, 'x': '#'}
    myFun.f1(*args, **kw)
    print(myFun.fact(100))
    # slice test start
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    print([L[0], L[1], L[2]])
    # slice
    print(L[0:2],L[:3])
    print(L[1:3])
    print(L[-1:])
    L = []
    print(L)
    L = [x * x for x in range(1, 11)]
    print(L)
    ##filter()函数用于过滤序列
    print(list(filter(myFun.is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
    print(sorted([36, 5, -12, 9, -21]))
    #闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
    f1 , f2, f3 = myFun.count()
    print(f1(),f2(),f3())
    # 多线程
    print('Process (%s) start...' % os.getpid())

    app = Application()
    # 设置窗口标题:
    app.master.title('Hello World')
    # 主消息循环:
    app.mainloop()