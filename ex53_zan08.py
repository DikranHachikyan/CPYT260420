# Global Definitions

# 1. дефиниция


if __name__ == '__main__':
    # 2.извикване
    actions = {
        '+': lambda a,b: a + b,
        '/': lambda a,b: a / b
    }

    while True:
        ch = input('Actions: +, /, q-quit:')
        
        if ch == 'q':
            break

        n1 = float(input('n1='))
        n2 = float(input('n2='))

        res = actions[ch]( n1, n2 )
        print(f'{n1} {ch} {n2} = {res}')

    print('--- end of script ---')