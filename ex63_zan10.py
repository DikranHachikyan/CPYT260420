# Global Definitions

# 1. дефиниция
class Point:
    
    def __init__(self, *, x=0, y=0, visible=True, **kwargs):
        '''Constructor'''
        print('--- Init Point ---')
        # данни на обекта
        self.set_x(x)        
        self.set_y(y)
        self.set_visible(visible)

    # Методи на обекта
    def show(self):
        print(f'show point at ({self.get_x()},{self.get_y()})')

    def move_to(self, dx, dy):
        self.set_x( self.get_x() + dx )
        self.set_y( self.get_y() + dy )

    # Методи за достъп до данните (класически вариант)
    def set_x(self, x):
        assert x >= 0, f'x must be positive number (x={x})'
        self.__x = x
    
    def set_y(self, y):
        assert y >= 0, f'y must be positive number (y={y})'
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y        

    def set_visible(self,visible):
        assert type(visible) is bool, 'Visible must be boolean'
        self.__visible = visible

    def is_visible(self):
        return self.__visible

if __name__ == '__main__':
    # 2. декларация на променлива от типа Point
    # клас - типа, който сме дефинирали (Point)
    # обект - променливата от тип Point (представител на класа)
    print('--- start of script ---')
    p1 = Point()
    p2 = Point(x=10, y=20)

    if p1.is_visible():
        p1.show()

    p1.set_x(10)
    p1.set_y(4)

    p1.show()

    # AssertionError: x must be positive number (x=-3)
    # p2.set_x(-3)
    # p2.set_visible('Yes')


    print('--- end of script ---')