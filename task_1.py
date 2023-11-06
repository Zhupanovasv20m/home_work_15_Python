# Возьмите любые 1-3 задания из прошлых домашних заданий. 
# Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из 
# командной строки с передачей параметров.

import logging
import argparse

logging.basicConfig(filename='logs.log', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


class NegativeValueError(Exception):
    pass


class Rectangle:

    def __init__(self, width, height=None):
        if width <= 0:
            logger.error(f'Ширина должна быть положительной, а не {width}')
            # raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                logger.error(f'Высота должна быть положительной, а не {height}')
                # raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height
        logging.info(f"Начало работы функции {Rectangle} c аргументами {width} и {height}.")
    
    @property 
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value


    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    
logging.info(f"Завершение работы функции {Rectangle}.")

def par():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', default=1)
    parser.add_argument('-m', '--mm', default=2)
    args = parser.parse_args()
    return Rectangle(args.number, args.mm)

a = Rectangle(-9, 4)
print(a)

print(par())

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='My test')
#     parser.add_argument('param', metavar='a b c', type=float, help='enter a b c separated by a space')
#     args = parser.parse_args()
#     print(Rectangle(*args.param))

