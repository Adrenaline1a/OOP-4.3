#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
import colorama
from colorama import Fore, Back, Style


"""
В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный
номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть
метод "иду за героем", который в качестве аргумента принимает объект типа "герой". У
героев есть метод увеличения собственного уровня.
В основной ветке программы создается по одному герою для каждой команды. В цикле
генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран. У
героя, принадлежащего команде с более длинным списком, увеличивается уровень.
Отправьте одного из солдат первого героя следовать за ним. Выведите на экран
идентификационные номера этих двух юнитов.
"""


class Human:
     def __init__(self, team, id):
         self.team = team
         self.id = id

class Hero(Human):
    def __init__(self, team, id):
        super().__init__(team, id)
        self.lvl = 0
        self.detachment = []

class Soldier(Human):
    def __init__(self, team, id):
        super().__init__(team, id)

    def move(self, hero):
        hero.detachment.append(self.id)


def main():
    hero1 = Hero(0, 0)
    hero2 = Hero(1, 1)
    teams ={
        hero1.team:{
            "id Героя":hero1.id,
            "id Солдат": []
        },
        hero2.team:{
            "id Героя":hero2.id,
            "id Солдат": []
        }
    }
    list_sold = {}
    for i in range(2, 12):
        team = random.randint(0, 1)
        list_sold[i] = Soldier(team, i)
        teams[team]["id Солдат"].append(i)
    
    if len(teams[hero1.team]["id Солдат"]) > len(teams[hero2.team]["id Солдат"]):
        hero1.lvl += 1
    elif len(teams[hero1.team]["id Солдат"]) < len(teams[hero2.team]["id Солдат"]):
        hero2.lvl += 1
    else:
        print(Fore.RED + "Уровни героев не меняются, т.к. одинаковое количество солдат в обеих командах")
    
    try:
        f_sold = teams[hero1.team]["id Солдат"][0]
        list_sold[f_sold].move(hero1)
    except:
        print(Fore.RED + "Команда первого героя пуста")
    
    print(Fore.WHITE + "Уровень героя первой команды: ", hero1.lvl, "\nУровень героя второй команды: ", hero2.lvl)
    print(Fore.WHITE + "Следуют за первым героем: ", hero1.detachment, "\nСледуют за вторым героем: ", hero2.detachment)


if __name__ == "__main__":
    colorama.init()
    main()
