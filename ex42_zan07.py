# Global Definitions

# 1. дефиниция
def sum_n(n):
    print(f'n={n}')

    if n > 0:
        return n + sum_n( n - 1 )
    return 0

if __name__ == '__main__':
    # 2.извикване
    result = sum_n(100)
    print(f'1 + 2 + 3 +...+ 99 + 100={result}')
    # result = sum_n(3)
    # print(f'1 + 2 + 3={result}')

    print('--- end of script ---')