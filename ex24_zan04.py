# Global Definitions

if __name__ == '__main__':
    config = {
        'title':'Text Editor',
        'version':'1.2.4',
        'printer': 'HP Laser Jet',
        'margins':[5, 10, 5, 10]
    }
    
    for key in config:

        if type(config[key]) in (str,int,bool,float):
            print(f'key={key} =>{config[key]}')
        elif type(config[key]) is list:
            print(f'key={key}')
            for value in config[key]:
                print(f'    value={value}')
        
    print('--- Last line of code --')