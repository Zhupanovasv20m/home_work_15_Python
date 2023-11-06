# Возьмите любые 1-3 задания из прошлых домашних заданий. 
# Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из 
# командной строки с передачей параметров.

import logging
import argparse

logging.basicConfig(filename='logs_two.log', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

class InvalidNameError(ValueError):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Invalid name: {self.name}. Name should be a non-empty string.'


class InvalidAgeError(ValueError):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'Invalid age: {self.age}. Age should be a positive integer.'


class InvalidIdError(ValueError):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return logger.error(f'Invalid id: {self.id}. Id should be a 6-digit positive integer between 100000 and 999999.')

logging.info('Начало работы программы')

class Person:
    
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        if not isinstance(last_name, str) or len(last_name.strip()) == 0:
            logger.error(f'Фамилия не должна быть пустой. Фамилия введена как ({last_name}).')
            raise InvalidNameError(last_name)
        if not isinstance(first_name, str) or len(first_name.strip()) == 0:
            logger.error(f'Имя не должно быть пустым. Имя введено как ({first_name}).')
            raise InvalidNameError(first_name)
        if not isinstance(patronymic, str) or len(patronymic.strip()) == 0:
            logger.error(f'Отчество не должно быть пустым. Отчество введено как ({patronymic}).')
            raise InvalidNameError(patronymic)
        if not isinstance(age, int) or age <= 0:
            logger.error(f'Возраст должен быть введен цифрами и не равен 0. Получено значение возраста: ({age}).')
            raise InvalidAgeError(age)

        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age
        logging.info(f"Получены данные о человеке с фамилией {self.last_name}, именем {self.first_name} и отчеством {self.patronymic}. Ему {self._age} лет.")

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'
    

    
    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    logging.info('Работа функции завершена')

class Employee(Person):
    MAX_LEVEL = 7

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, id: int):
        super().__init__(last_name, first_name, patronymic, age)
        if not isinstance(id, int) or id < 100_000 or id > 999_999:
            # logger.error(f'ID должен содержать 6 цифр в диапазоне от 100000 до 999999.')
            raise InvalidIdError(id)

        self.id = id
        logging.info(f'Для сотрудника с ФИО {last_name, first_name, patronymic} получен ID {self.id}')

    def get_level(self):
        s = sum(num for num in str(self.id))
        return s % self.MAX_LEVEL
    
    logging.info('Работа функции {__init__} завершена')

a = Person('rg', 'fff', 'ryr', 30)
b = Employee('EE', 'yy', 'ryr', 70, 454656)

def par():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--last', default="None")
    parser.add_argument('-f', '--first', default="None")
    parser.add_argument('-p', '--patronymic', default="None")
    parser.add_argument('-a', '--age', default=18)
    args = parser.parse_args()
    return Person(args.last, args.first, args.patronymic, args.age)


print(par())