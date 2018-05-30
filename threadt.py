import time,threading,multiprocessing

balance =0

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
    print(balance)

local_school = threading.local()
def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
'''local_school看成全局变量
属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰
'''
def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()
## main
if __name__=="__main__":
  print('=======main======')
  print('thread %s is running...' % threading.current_thread().name)
  t = threading.Thread(target=loop, name='LoopThread')
  t.start()
  t.join()
  print('thread %s ended.' % threading.current_thread().name)
  #run_thread(5)
  print('=====muti process cpu=====')
  for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

  t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
  t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
  t1.start()
  t2.start()
  t1.join()
  t2.join()