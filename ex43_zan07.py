# Global Definitions

# 1. дефиниция


if __name__ == '__main__':
    # 2.извикване
    pow_xy = lambda x,y: x ** y

    z = pow_xy(2, 4)
    print(f'z={z}')

    numbers = [2, 4, 6, 3, 1]

    for v  in map( lambda el: el ** 2, numbers ):
        print(f'v={v}')

    print('--- end of script ---')