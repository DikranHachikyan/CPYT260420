# Global Definitions


if __name__ == '__main__':
    i = 1
    sum_n = 0
    is_interrupted = True

    while i <= 100:
        sum_n += i
        if sum_n > 15:
            break
        i += 1
    else:
        is_interrupted = False
        print('--- else ---')

    print(f'1+2+3+ ... +99+100={sum_n}, interrupted:{is_interrupted}')
    
    print('--- Last line of code --')