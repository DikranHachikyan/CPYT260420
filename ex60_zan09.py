# Global Definitions

# 1. дефиниция
class Point:
    
    def __init__(self):
        '''Constructor'''
        print('--- Init Point ---')
        # данни на обекта
        self.x = 10
        self.y = 20

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
    p = Point()
    
    print(f'type of p is {type(p)}, point at ({p.x},{p.y})')
    
    p.show()
    p.move_to(-3, 4)
    p.show()

    print('--- end of script ---')