# Global Definitions

# 1. дефиниция
def foo(values, n):
    n **= 2
    print(f'inside foo: id={id(n)}, n={n}')

    values.sort(reverse=True)
    print(f'inside foo: id={id(values)}, values={values}')


if __name__ == '__main__':
    # 2.извикване
    # mutable
    numbers = [ 6, 3, 1, 4]
    # immutable
    a = 10

    print(f'(before) numbers (id={id(numbers)}, numbers={numbers}) a (id={id(a)}, a={a})')

    foo(numbers, a)

    print(f'(after) numbers (id={id(numbers)}, numbers={numbers}) a (id={id(a)}, a={a})')
    
    print('--- end of script ---')