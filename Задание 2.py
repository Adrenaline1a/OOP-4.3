#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Создать класс Liquid (жидкость), имеющий поля названия и плотности. Определить методы
переназначения и изменения плотности. Создать производный класс Аlcohol (спирт),
имеющий крепость. Определить методы переназначения и изменения крепости.
"""


class Liquid:
    def __init__(self, name, density):
        self.__name = name
        self.__density = density

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, inp):
        self.__name = inp

    @property
    def density(self):
        return self.__density

    @density.setter
    def density(self, inp):
        self.__density = inp


class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self.__strength = strength

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, inp):
        self.__strength = inp


def main():
    a1 = Alcohol("Водка", 949, 30)
    l1 = Liquid("Вода", 1000)
    print(a1.name, a1.density, a1.strength)
    print(l1.name, l1.density)
    a1.strength = 60
    print(a1.name, a1.density, a1.strength)


if __name__ == "__main__":
    main()
