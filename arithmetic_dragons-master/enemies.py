# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_enemy_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list
    
def IsPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n
    
def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return ', '.join(map(str, Ans))
    
    
class Dragon(Enemy):
    _type = 'дракон'

class Troll(Enemy):
    _type = 'тролль'


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(str(x + y))
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1, x + 1)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(str(x - y))
        return self.__quest
        
class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'чёрный'

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(str(x * y))
        return self.__quest
        
class WhiteTroll(Troll):
    def __init__(self):
        self._health = 50
        self._attack = 5
        self._color = 'белый'

    def question(self):
        x = randint(1,5)
        self.__quest = 'Угадай число от 1 до 5'
        self.set_answer(str(x))
        return self.__quest

class YellowTroll(Troll):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'желтый'

    def question(self):
        x = randint(1,100)
        self.__quest = 'Число: ' + str(x) + ' простое(True) или нет(False)'
        self.set_answer(str(IsPrime(x)))
        return self.__quest

class PinkTroll(Troll):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'розовый'

    def question(self):
        x = randint(2,100)
        self.__quest = 'Разложите число: ' + str(x) + ' на множители'
        self.set_answer(Factor(x))
        return self.__quest


enemy_types = [GreenDragon, RedDragon, BlackDragon, 
               WhiteTroll, YellowTroll, PinkTroll]
