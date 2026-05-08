# Global Definitions

# 1. дефиниция
def sort_priority( values, pri_group):
    found = False

    def sort_helper(el):
        nonlocal found
        if el in pri_group:
            found = True
            return (0, el)
        return (1, el)

    values.sort( key=sort_helper )
    return found

if __name__ == '__main__':
    # 2.извикване
    numbers = [5, 3, 4, 6, 7, 8, 9, 2 ]
    group = {3, 8, 9}

    is_found = sort_priority( numbers, group)
    
    print(f'numbers:{numbers} is found:{is_found}')

    print('--- end of script ---')