"""
Module 'classes' created as a part of
solution to exercises from course
'OOP Python'
"""
import re
import math
import random
from math import pi


class Warrior:
    """
    Creates Warrior.
    Accepts Warrior name.
    """

    # instances of class Warrior
    count = 0

    def __init__(self, name=None):
        self.__health = 100
        Warrior.count_up()
        name2 = f'{Warrior.count}Warrior'
        self.__name = name or name2

    def __repr__(self):
        return self.__name

    def __setattr__(self, attr, value):
        """
        Allows setting values to
        '_Warrior__health', '_Warrior__name'
        attributes only.
        Else raises AttributeError
        """
        attributes = ('_Warrior__health', '_Warrior__name')

        if attr in attributes:
            self.__dict__[attr] = value
        else:
            raise AttributeError

    def count_up():
        """
        Incresing number of Warrior instances by one
        """
        Warrior.count += 1

    def get_health(self):
        return self.__health

    def get_name(self):
        return self.__name

    def isalive(self):
        return self.__health > 0

    def attack(self, warr):
        """
        'self' instance attacs 'warr' and
        as a result 'warr' gets minus 20 from
        'health'
        """
        if warr.isalive():
            print(f'{self} attacks {warr}')
            warr.sub_health()
        else:
            print(f'{warr} is already dead! Stop trying to kill him!')

    def sub_health(self, v=20):
        """
        Substracting 20 'health' from 'self'
        """
        self.__health -= v

        if self.isalive():
            print(f'{self} gets minus {v} helth. Left {self.__health}\n')
        else:
            print(f'{self} is dead!')


class Person:
    """
    Stores employee data like
    (first_name, last_name, qualification)
    """

    def __init__(self, first_name, last_name, qual=1):
        self.first_name = first_name
        self.last_name = last_name
        self.qual = qual

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.qual}'

    def __del__(self):
        print(f'Goodbye mister {self.first_name} {self.last_name}')


class Unit:
    """
    Attributes:
    num - unique number
    team - group name to which unit
    belongs
    """

    __count = 0

    def __init__(self, team=None):
        Unit.__count_up()
        self.num = Unit.__count
        self.team = team

    def __count_up():
        Unit.__count += 1

    def className(self):
        pattern = re.compile(r'^<class \'__\w+__\.(\w+)\'>')
        return pattern.match(str(self.__class__)).group(1)

    def __str__(self):
        return f'{self.num}{self.className()}'


class Hero(Unit):
    """
    Attribute: level by default 1
    """
    def __init__(self, team, level=1):
        super().__init__(team)
        self.__level = level

    def get_level(self):
        return self.__level

    def level_up(self, by=1):
        self.__level += by
        print(f'{self} gets a raise. Level: {self.__level}')


class Soldier(Unit):

    def follow_hero(self, hero):
        print(f'I am {self} following {hero}')


class Num:
    """
    Attributes:
    'num' - number.
    """
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        """
        Returns new 'Num' instance
        """
        return Num(self.num + other.num)

    def __str__(self):
        return f'Num {self.num}'


class Win_Door:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return self.x * self.y


class Room:
    def __init__(self, length, width, height):
        self.x = length
        self.y = width
        self.z = height
        self.wd = []

    def square(self):
        return 2 * self.z * (self.x + self.y)

    def addWD(self, width, hight):
        self.wd.append(Win_Door(width, hight))

    def workSurface(self):
        new_square = self.square()
        for i in self.wd:
            new_square -= i.square()
        return new_square

    def numRolls(self, width, hight):
        one_roll = width * hight
        square = self.workSurface()
        return math.ceil(square / one_roll)


class Snow:
    """
    Attributes:
    flakes(int) - number of flakes
    """
    def __init__(self, flakes: int):
        self.flakes = flakes

    def getFlakes(self):
        return self.flakes

    def __add__(self, n):
        self.flakes += n
        return self.flakes

    def __sub__(self, n):
        self.flakes -= n
        return self.flakes

    def __mul__(self, n):
        self.flakes *= n
        return self.flakes

    def __truediv__(self, n):
        self.flakes //= n
        return self.flakes

    def __call__(self, n):
        self.flakes = n

    def makeSnow(self, n):
        """
        returns string of '*' symbols
        where number of asteriks in one
        row equals 'n'. Rows are separated
        by '\n'
        """
        rows = self.flakes // n
        numLeftFlakes = self.flakes % n

        snowFall = ''

        snowFall = ''.join(
            ['*' * n + '\n' for _ in range(rows)]
            )

        snowFall += numLeftFlakes * '*'

        return snowFall


class Data:
    """
    Stores list of subjects by name.
    Created for usage with classes:
    'Teacher', 'Pupil'.
    """
    def __init__(self, *info):
        self.info = list(info)

    def __getitem__(self, i):
        return self.info[i]

    def __str__(self):
        return str(self.info)


class Teacher:
    """
    'Teacher' teacher 'Pupil'.
    Created for usage with classes:
    'Data', 'Pupil'.
    """
    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)


class Pupil:
    """
    Pupil learns new information either
    by himself or with teacher. Able to
    forget learnd.
    Created for usage with classes:
    'Teacher', 'Data'.
    """
    def __init__(self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)

    def selfEduc(self, info):
        self.knowledge.append(info)

    def randomForget(self):
        n = random.randint(0, len(self.knowledge) - 1)
        print(f"{self.knowledge.pop(n)} item is succesfully forgotten!")


class Cylinder:
    """
    Stores diameter and hight of a cylinder.
    Allows to compute area of it.
    """
    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle*2 + side, 2)

    def __init__(self, diameter, high):
        self.dia = diameter
        self.h = high
        self.__area = self.make_area(diameter, high)

    def __setattr__(self, attr, value):
        if attr in ['dia', 'h', '_Cylinder__area']:
            self.__dict__[attr] = value
        else:
            raise AttributeError

        shape_params = set(('dia', 'h'))
        self_attr = set(self.__dict__.keys())
        if attr in shape_params and self_attr.issuperset(shape_params):
            self.__area = self.make_area(self.dia, self.h)

    def __str__(self):
        s = f"Cylinder area = {self.__area} "\
            f"with diamiter = {self.dia} "\
            f"and hight = {self.h}"
        return s

    def getArea(self):
        return self.__area
