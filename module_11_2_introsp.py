import sys
from pprint import pprint
import inspect

# 'Тачка' из задания
class Vehicle:
    __COLOR_VARIANTS = ['red','green','blue','black','white','purple','yellow']
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        color = color.lower()
        if color in self.__COLOR_VARIANTS:
            self.__color = color
        else:
            print("Такого цвете нет в списка цветов, белым будешь")
            self.__color = 'white'

    def get_model(self):
        print(f'Модель {self.__model}')
    def get_horsepower(self):
        print(f'Мощность двигателя {self.__engine_power}')
    def get_color(self):
        print(f'Цвет: {self.__color}')
    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец; {self.owner}')

    def set_color(self,color):
        color = color.lower()
        if color in self.__COLOR_VARIANTS:
            self.__color = color
            print(f'Тачку перекрасили в {color}')
        else:
            print(f'Нельзя сменить цвет на {color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


def  introspection_info(obj):
    rez={}
    try:
        vars_ = vars(obj)
    except:
        vars_=['...']

    rez.update({'type':type(obj),
                'attributes':vars_,
                'methods':dir(obj),
                'module':sys.modules
                })
    return rez

if __name__ == '__main__':
    car1 = Sedan('Кодер Вася', 'ВАЗ 2104', 'white', 70)
    inf_=introspection_info(car1)
    pprint(inf_)

