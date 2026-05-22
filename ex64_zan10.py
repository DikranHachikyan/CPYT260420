# Global Definitions

# 1. дефиниция
class Point:
    
    def __init__(self, *, x=0, y=0, visible=True, **kwargs):
        '''Constructor'''
        print('--- Init Point ---')
        # данни на обекта
        self.x = x        
        self.y = y
        self.is_visible = visible

    # Методи на обекта
    def show(self):
        print(f'show point at ({self.x},{self.y})')

    def move_to(self, dx, dy):
        self.x += dx 
        self.y += dy

    # Методи за достъп до данните (python)
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,x):
        assert x >= 0, f'x must be positive number (x={x})'
        self.__x = x
    
    @property
    def y(self):
        return self.__y        
    
    @y.setter
    def y(self, y):
        assert y >= 0, f'y must be positive number (y={y})'
        self.__y = y

    @property
    def is_visible(self):
        return self.__visible

    @is_visible.setter
    def is_visible(self,visible):
        assert type(visible) is bool, 'Visible must be boolean'
        self.__visible = visible


if __name__ == '__main__':
    # 2. декларация на променлива от типа Point
    # клас - типа, който сме дефинирали (Point)
    # обект - променливата от тип Point (представител на класа)
    print('--- start of script ---')
    p1 = Point()
    p2 = Point(x=10, y=20)

    if p1.is_visible:
        p1.show()

    p1.x = 10
    p1.y = 4

    p1.show()

    # AssertionError: x must be positive number (x=-3)
    # p2.x = -3
    # p2.is_visible = 'Yes'


    print('--- end of script ---')