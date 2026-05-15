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
def to_str(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        args = [ f'{v}' for v in args]
        return func(*args, **kwargs)
    return wrapper

def add_brackets(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = [ f'[{v}]' for v in args]
        return func(*args, **kwargs)
    return wrapper

@add_brackets
@to_str
def concat(*args,**kwargs):
    '''Concatenate args with separator sep'''
    sep = kwargs.get('sep', ';')

    return sep.join(args)


if __name__ == '__main__':
    users = ['anna', 'maria', 'markus', 'jorg']

    print(f'users: {concat(*users)}')    
    print(f'users: {concat(*users, sep=", ")}')

    values = [ 10, 20, 30, 55, 35]
    print(f'values: {concat(*values, sep="|")}')

    print('--- end of script ---')