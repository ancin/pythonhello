def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

def my_abs(x):
    if x>0:
        return x
    else:
        return -x

def calc(numbers):
  sum =0
  for i in numbers:
    sum = sum + i*i
  return sum

#可变参数 *args是可变参数，args接收的是一个tuple
def calc2(*numbers):
  sum =0
  for i in numbers:
    sum = sum + i*i
  return sum

# 关键字参数，**kw接收的是一个dict。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# 命名关键字参数
def person2(name,age,**kw):
  if 'city' in kw:
    pass
  if 'job' in kw:
    pass
  print('name:', name, 'age:', age, 'other:', kw)

# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

#递归
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
##斐波拉契数列用列表生成式
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
#传入函数
def getAdd(x, y, f):
    return f(x) + f(y)
def add(x, y, f):
    return f(x) + f(y)
def is_odd(n):
    return n % 2 == 1

#闭包
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


class Student(object):

  def __init__(self,name,score):
    self.__name = name
    self.__score = score
 # __slots__ = ('area', 'address') # 用tuple定义允许绑定的属性名称
  @property
  def score(self):
      return self.__score

  def print_score(self):
      print('%s: %s' % (self.__name, self.__score))

  def __str__(self):
    return 'Student object (name: %s)' % self.__name