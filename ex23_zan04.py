# Global Definitions

if __name__ == '__main__':
    users = [
        'Anna',
        'Maria',
        'Markus',
        'Jorg'
        'Florian'
    ]
    
    emails = [
        'anna@no.com',
        'maria@no.com',
        'markus@no.com',
        'jorg@no.com',
        'florian@no.com'
    ]
    
    for data in zip( users, emails ):
        name, email = data
        print(f'data={data}, user={name} email={email}')
        
    print('--- Last line of code --')