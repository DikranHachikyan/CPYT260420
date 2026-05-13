# Global Definitions

# 1. дефиниция


if __name__ == '__main__':
    # 2.извикване
    actions = {
        '+': lambda a,b: a + b,
        'q': lambda a,b: quit()
    }

    while True:
        n1 = float(input('n1='))
        n2 = float(input('n2='))

        ch = input('Actions: +, q-quit:')

        if ch in '+q':
            res = actions[ch]( n1, n2 )
            print(f'{n1} {ch} {n2} = {res}')

    print('--- end of script ---')