# Global Definitions
# port - глобална променлива
port = 1521

# 1. дефиниция
def sum_numbers(a, b):
    # c - локална променлива
    c = a + b
    return c


if __name__ == '__main__':
    # 2.извикване
    res = sum_numbers(5, 6)
    print(f'res={res}')
    
    x, y = 7, 8
    res = sum_numbers(x, y)
    print(f'{x} + {y} = {res}')
    
    print('--- end of script ---')