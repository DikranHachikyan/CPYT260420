# Global Definitions

# 1. дефиниция


if __name__ == '__main__':
    # 2.извикване
    actions = {
        '+': lambda a,b: a + b,
        '/': lambda a,b: a / b
    }

    while True:
        try:
            ch = input('Actions: +, /, q-quit:')
            
            if ch == 'q':
                break

            n1 = float(input('n1='))
            n2 = float(input('n2='))
            res = actions[ch]( n1, n2 )
            
        except KeyError as e:
            print(f'Unsupported operation: {e}!')
        except ValueError as e:
            print(f'Invalid number! ({e})')
        # except:
        except Exception as e:
            print(f'Unknown error!({e})')
        # 1. python only
        else:
            print(f'{n1} {ch} {n2} = {res}')

    print('--- end of script ---')