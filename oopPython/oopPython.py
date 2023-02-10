"""
In script 'oopPython' I explore OOP concepts
in Python language by instantiating classes
from 'classes.py' and testing them. Exersises taken
from course 'OOP Python'
"""
import random
from classes import *


def biggerTeamAction(t1, t2, l1, l2, sold, h):

    print(f"{t1} team has more soldiers ({l1}) than {t2} team ({l2})")
    sold.follow_hero(h)
    h.level_up()


def StrategyGame():
    """
    Creates two 'Hero' and
    random number of 'Soldier'
    that divided into teams randomly.
    Team with bigger amount of soldiers
    wins.
    """
    n_sold = random.randint(5, 20)

    team_names = ('red', 'green')

    h1 = Hero(team_names[0])
    h2 = Hero(team_names[1])

    team1, team2 = [], []

    for i in range(n_sold):
        team = random.choice(team_names)
        sold = Soldier(team)
        if team == team_names[0]:
            team1.append(sold)
        else:
            team2.append(sold)

    l1, l2 = len(team1), len(team2)
    if l1 > l2:
        biggerTeamAction(team_names[0], team_names[1], l1, l2, team1[0], h1)
    elif l1 < l2:
        biggerTeamAction(team_names[1], team_names[0], l2, l1, team2[0], h2)
    else:
        print(f"Having equalent number of soldiers in both teams ({l1})")


def Battle():
    """
    Conduct battle between two instances
    of class 'Warrior'
    """
    warriors = [Warrior(), Warrior()]

    while warriors[1].isalive():
        random.shuffle(warriors)
        warriors[0].attack(warriors[1])

    print(f'\n!!!{warriors[0]} wins!!!')


def Hire_and_fire():
    """
    Imitates hiring and firing proccess
    """

    p1 = Person('Tsimafei', 'Khamitsevich', 2)
    p2 = Person('Max', 'Cherenzov', 3)
    p3 = Person('John', 'Green')

    for i in (p1, p2, p3):
        print(i)

    del p3, i
    input()


def collectUserInput(params):
    for key in params.keys():
        while True:
            print(f"Enter {key}")
            user_input = input()
            if user_input.isdigit():
                params[key] = int(user_input)
                break
            else:
                print('Input is incorect. Please, try again.')


def room_init():
    """
    Collecting data from user
    about window/door in room
    """

    print("Now, I need parameteres of you room.")

    room_params = dict.fromkeys(('length', 'width', 'height'))

    collectUserInput(room_params)
    return Room(**room_params)


def win_door_init(room):
    """
    Collecting data from user
    about window/door in room
    """
    print('Now, I need number of door/window in you room.')
    num_wd = {'number': None}
    collectUserInput(num_wd)
    wd_params = dict.fromkeys(('width', 'hight'))
    for i in range(1, num_wd['number'] + 1):
        print('Enter parameters of door/window number %d' % (i))
        collectUserInput(wd_params)
        room.addWD(**wd_params)


def wallpaper_init(room):
    """
    Collects data from user
    about wallpaper size.
    Returns number wallpaper rolls
    needed for room
    """
    print('Now, I need to now parameters of one wallpaper roll')
    wallpaper_params = dict.fromkeys(('width', 'hight'))
    collectUserInput(wallpaper_params)

    return room.numRolls(**wallpaper_params)


def calcWallpapers():
    """
    Collecting from user data about room,
    window/door, wallpaper to compute:
    - square area of walls in room
    - number of wallpaper rolls needed
    """
    message = """Hi, I will help you to count square area
    of walls and number of rolls you will need."""
    print(message)

    room = room_init()
    win_door_init(room)

    print(f"Square area of walls in your room equals {room.square()}")

    num_wp = wallpaper_init(room)
    print(f"{num_wp} wallpaper rolls you will need for you room")
    print('Happy wallpaper installation')


def Add_nums():
    """
    Creates new 'Num' instance from
    two 'Num' instances.
    """
    n1 = Num(7)
    n2 = Num(4)
    n3 = n1 + n2
    print(n3)


def PlayingSnow():
    """
    Testing functionality of
    class 'Snow'
    """
    snow = Snow(88)
    print(snow + 9)
    print(snow - 90)
    print(snow * 10)
    print(snow / 4)
    snow(100)
    print(snow.getFlakes())
    print(snow.makeSnow(9))


def TeacherStudent():
    """
    Testing 'Data', 'Teacher', 'Pupil'
    classes.
    """
    data = Data(['Python', 'SQL', 'Esoteric', 'Philosopy'])
    Rob = Teacher()
    Bob = Pupil()
    print(data)
    Rob.teach(data[0][0], Bob)
    Rob.teach(data[0][2], Bob)
    Bob.selfEduc(data[0][1])
    print(Bob.knowledge)
    Bob.randomForget()


def CylinderArea():
    """
    Testing class Cylinder
    """
    cylinder = Cylinder(3, 6)
    print(cylinder)
    cylinder.dia = 10
    print(cylinder)


if __name__ == '__main__':
    # list of Functions to try:
    CylinderArea()
    # TeacherStudent()
    # PlayingSnow()
    # calcWallpapers()
    # Add_nums()
    # StrategyGame()
    # Hire_and_fire()
    # Battle()
