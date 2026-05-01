# Global Definitions

if __name__ == '__main__':
    values = [ i**2 for i in range(10)]

    print(f'values:{values}')

    txt = 'lorem ipsum dolor sit'

    symb = [f'-{s}-' for s in txt]

    print(f'symbols={symb}')

    print('--- Last line of code --')

    values = [ f'(i={i},j={j})' for i in range(3) for j in range(4)]

    # for i in range(3):
    #     for j in range(4):
    #         print(f'({i},{j})')

    print(f'values={values}')
