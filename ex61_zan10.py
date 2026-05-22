# Global Definitions

# 1. дефиниция
class Point:
    
    def __init__(self, *, x=0, y=0, **kwargs):
        '''Constructor'''
        print('--- Init Point ---')
        # данни на обекта
        self.x = x
        self.y = y

    # Методи на обекта
    def show(self):
        print(f'show point at ({self.x},{self.y})')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

if __name__ == '__main__':
    # 2. декларация на променлива от типа Point
    # клас - типа, който сме дефинирали (Point)
    # обект - променливата от тип Point (представител на класа)
    print('--- start of script ---')
    p1 = Point()
    p2 = Point(x=10, y=20)

    p1.show()
    p2.show()
    
    p1.move_to(-3, 4)
    p1.show()


    print('--- end of script ---')