#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod
from cmath import pi


"""
Создать абстрактный базовый класс Body (тело) с абстрактными функциями вычисления
площади поверхности и объема. Создать производные классы: Parallelepiped
(параллелепипед) и Ball (шар) со своими функциями площади поверхности и объема.
"""


class Body(ABC):

    @abstractmethod
    def square(self):
        pass
    
    @abstractmethod
    def volume(self):
        pass


class Ball(Body):
    def square(self, R):
        print("Площадь поверхности шара: ", 4*pi*R**2)
    
    def volume(self, R):
        print("Объём шара: ", 4/3*pi*R**3)


class Parallelepiped(Body):
    def square(self, a, b, c):
        print("Площадь поверхности параллелепипеда: ", 2*(a*b + b*c + a*c))
    
    def volume(self, a, b, c):
        print("Объём параллелепипеда: ", a*b*c)


def main():
    b1 = Ball()
    b1.square(1)
    p1 = Parallelepiped()
    p1.square(1, 1, 1)
    b1.volume(1)
    p1.volume(1, 1, 1)


if __name__ == "__main__":
    main()