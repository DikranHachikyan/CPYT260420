# Global Definitions

# 1. дефиниция
class Point:
    
    def __init__(self, *, x=0, y=0, **kwargs):
        '''Constructor'''
        print('--- Init Point ---')
        # данни на обекта
        self.__x = x
        self.__y = y

    # Методи на обекта
    def show(self):
        print(f'show point at ({self.__x},{self.__y})')

    def move_to(self, dx, dy):
        self.__x += dx
        self.__y += dy

if __name__ == '__main__':
    # 2. декларация на променлива от типа Point
    # клас - типа, който сме дефинирали (Point)
    # обект - променливата от тип Point (представител на класа)
    print('--- start of script ---')
    p1 = Point()
    p2 = Point(x=10, y=20)

    # p1.x = -100
    # p1.y = 120
    # print(f'p1: x={p1.__x}, y={p1.__y}')
    # AttributeError: 'Point' object has no attribute '__x'

    # В Python атрибутите могат да се "закачат" динамно
    # p1.z = 20
    # print(f'p1: z={p1.z} p2: z={p2.z}')

    p1.show()
    p2.show()
    
    p1.move_to(30, 4)
    p1.show()


    print('--- end of script ---')