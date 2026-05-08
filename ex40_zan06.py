# Global Definitions

# 1. дефиниция
def foo(a=[], b={}):
    print(f'a={a}, b={b}')
    print('-' * 50)

    n = len(a)
    a.append(n)
    b[n] = n



if __name__ == '__main__':
    # 2.извикване
    foo()

    foo([2,4,6], {'z':10})

    foo()

    foo([4, 6, 1], {'x':20})
    
    foo()
    
    foo()


    print('--- end of script ---')