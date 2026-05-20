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
                # quit()

            n1 = float(input('n1='))
            n2 = float(input('n2='))
            res = actions[ch]( n1, n2 )
            
        except (KeyError, ValueError) as e:
            print(f'Unsupported operation or invalid number: {e}!')
        # # except:
        except Exception as e:
            print(f'Unknown error!({e})')
        # 1. python only
        else:
            print(f'{n1} {ch} {n2} = {res}')
        # 2. python (not only)
        finally:
            print(f'--- finally ---')

    print('--- end of script ---')