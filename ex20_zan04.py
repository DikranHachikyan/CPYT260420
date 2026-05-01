# Global Definitions


if __name__ == '__main__':
    values = 12, 34, 56, 78, 89

    for item in enumerate( values ):
        key, value = item
        print(f'key={key}, value={value}')
        
    print('--- Last line of code --')