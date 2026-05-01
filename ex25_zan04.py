# Global Definitions

if __name__ == '__main__':
    config = {
        'title':'Text Editor',
        'version':'1.2.4',
        'printer': 'HP Laser Jet',
        'margins':[5, 10, 5, 10]
    }
    
    for item in config.items():
        key, value = item
        print(f'key={key} =>{value}')
    else:
        print('--- else ---')
        
    print('--- Last line of code --')