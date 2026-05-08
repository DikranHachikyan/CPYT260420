# Global Definitions
port = 1521

# 1. дефиниция
def show():
    global port
    # c - локална променлива
    c = 10
    port = 1111
    print(f'local var:{c} port:{port}')

if __name__ == '__main__':
    # 2.извикване
    print(f'(before) global variable port:{port}')
    show()
    print(f'(after) global variable port:{port}')
    print('--- end of script ---')