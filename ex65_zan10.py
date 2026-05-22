
import draw.point as dp

if __name__ == '__main__':
    # 2. декларация на променлива от типа Point
    # клас - типа, който сме дефинирали (Point)
    # обект - променливата от тип Point (представител на класа)
    print('--- start of script ---')
    p1 = dp.Point(x=10, y=20)
    p2 = dp.Point(x=10, y=20)

    print(f'Object p2:{p2}')
    print(f'p2 coords:' + str(p2))

    # if p1.x == p2.x and p1.y == p2.y:
    if p1 == p2:
        print(f'1: {p1} equals to {p2}')
    else:
        print(f'2: {p1} does not equal to {p2}')

    p3 = p1 + p2
    p3.show()
    p3 = p1 + 10.5
    p3.show()
    
    print('--- end of script ---')