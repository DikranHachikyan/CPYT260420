# Global Definitions
# 1.
# import time
# print(f'now is:{time.time()}')

# 1.1
# import time as tm
# print(f'now is:{tm.time()}')

# 2.
# from time import time, sleep
# print(f'now is:{time()}')

# 2.1
# from time import time as now, sleep
# print(f'now is:{now()}')

from time import time, sleep
from functools import wraps

# 1. дефиниция на декоратора
def measure_time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        t = time()
        func(*args,**kwargs)
        print(f'1: name={func.__name__} docstr={func.__doc__} time={time()-t:.3f}')

    return wrapper

# 2. прилагаме декоратора
@measure_time
def foo(*,sleep_time=0.5):
    '''Function foo sleeps sleep_time seconds'''
    sleep(sleep_time)

if __name__ == '__main__':
    
    
    foo()


    foo(sleep_time=0.9)

    print(f'2: name={foo.__name__} docstr={foo.__doc__}')
    
    print('--- end of script ---')