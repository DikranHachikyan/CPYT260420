# Global Definitions

# 1. дефиниция
def print_key(*,key,**kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError as e:
        raise
        # още по-лоша идея!
        # pass

        # лоша идея!
        # print(f'Invalid Key!{e}')
    print('end of print_key')


if __name__ == '__main__':
    # 2.извикване
    conn = {
        'host':'localhost',
        'port':1521,
        'service': 'oracle-xe'
    }
    try:
        print_key(key='host', **conn)
        print_key(key='ip', **conn)
    except Exception as e:
        print(f'Error during execution!{e}')

    print('--- end of script ---')