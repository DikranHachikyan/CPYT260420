# Global Definitions

# 1. дефиниция
def show(title, *, ver='1.1.1', **kwargs):

    print(f'title (positional):{title}')

    print(f'ver (keyword only): {ver}')
    
    kw = {
        'color': kwargs.get('color','black'),
        'font': kwargs.get('font','sans-serif'),
        'size': kwargs.get('size', 16),
    }
    print(f'keyword args:{kw}')
    print()

if __name__ == '__main__':
    # 2.извикване
    arr = [1, 2, 3, 4, 5]
    ui = {
        'size':10, 
        'font':'Monospace', 
        'color':'red', 
        'platform':'phone',
        'width': 800
    }
    # keyword only arguments
    show('Web App', ver='2.2.2', **ui )
    print('---')
    show('Web App', **ui )


    print('--- end of script ---')