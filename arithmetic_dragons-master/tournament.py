# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, enemy_list):
    for enemy in enemy_list:
        print('Вышел', enemy._color, enemy._type, '!')
        while enemy.is_alive() and hero.is_alive():
            print('Вопрос:', enemy.question())
            answer = input('Ответ: ')

            if enemy.check_answer(answer):
                hero.attack(enemy)
                print('Верно! \n**', enemy._type, 'кричит от боли **')
            else:
                enemy.attack(hero)
                print('Ошибка! \n** вам нанесён удар, ваше здоровье: ', hero._health)
        if enemy.is_alive():
            break
        print(enemy._type, enemy._color, 'повержен!\n')
        hero._experience += 50

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())
        
        dragon_number = annoying_input_int('Введите колличество врагов: ')
        enemy_list = generate_enemy_list(dragon_number)
        assert(len(enemy_list) == dragon_number)
        print('У Вас на пути', dragon_number, 'драконов!')
        game_tournament(hero, enemy_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
