# Возьмите любые 1-3 задания из прошлых домашних заданий. 
# Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из 
# командной строки с передачей параметров.

'''
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.

'''
import logging
import argparse

logging.basicConfig(filename='logs_all.log', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


a = int(input('Введите сторону а: '))
b = int(input('Введите сторону b: '))
c = int(input('Введите сторону c: '))

logging.info(f"The values of a = {a}, of b = {b} and c = {c}.")


class InvalidZeroValue(Exception):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def err(self):
        return f'Аргументы не должны быть равны 0 и не могут быть отрицательными'

class InvalidValue(Exception):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def err(self):
        return f'Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.'


try:

    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            logging.info(f"Данный треугольник является - равносторонним со сторонами {a, b, c}")
            print('Данный треугольник является - равносторонним')
        elif a == b or b == c or a == c:
            logging.info(f"Данный треугольник является - равнобедренным со сторонами {a, b, c}")
            print('Данный треугольник является - равнобедренным')
        else:
            logging.info(f"Данный треугольник является - разносторонним со сторонами {a, b, c}")
            print('Данный треугольник является - разносторонним')
    elif a <= 0 or b<=0 or c<=0:
        logging.error(f'Получена ошибка {InvalidZeroValue} при аргументах {a, b, c}. Аргументы не должны быть равны 0 и не могут быть отрицательными')
        raise InvalidZeroValue
    else:
        logging.error(f'Получена ошибка {InvalidValue} при аргументах {a, b, c}. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.')
        raise InvalidValue
except Exception as e:
    logging.error(f'Получена ошибка {e} при аргументах {a, b, c}')


def par():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--a', default=1)
    parser.add_argument('-b', '--b', default=1)
    parser.add_argument('-c', '--c', default=1)
    args = parser.parse_args()
    return args.a, args.b, args.c