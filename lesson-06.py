# ДЗ к 6 уроку
#
#
# Easy
#
# Задачи № 1 и 2

class AllCar: #Можно сразу задать одним из типов машин, например TownCar и сократить код на 2 строки
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Машина {} начала движение.'.format(self.name))

    def stop(self):
        print('Машина {} остановилась.'.format(self.name))

    def turn(self, direction):
        print('Машина {} повернула {}!'.format(self.name, direction))

class TownCar(AllCar):
    def __init__(self, speed, color, name):
        AllCar.__init__(self, speed, color, name)

class WorkCar(AllCar):
    def __init__(self, speed, color, name):
        AllCar.__init__(self, speed, color, name)

class SportCar(AllCar):
    def __init__(self, speed, color, name):
        AllCar.__init__(self, speed, color, name)

class PoliceCar(AllCar):
    def __init__(self, speed, color, name, is_police=True):
        AllCar.__init__(self, speed, color, name)
        self.is_police = is_police

car = AllCar(120, 'Red', 'Audi')
car.go()
car.turn('Left')
car.stop()


# Nornal
#
# Задание № 1

import random

class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _atk_damage(self, damage):
        if self.armor > 0:
            self.armor = self.armor - damage
            if self.armor <= 0:
                self.armor = 0
        else:
            self.health = self.health - damage
            if self.health <= 0:
                self.health = 0

        print('{} наносит урон {}. HP - {}, ARM - {}'.format(self.name, self. damage, self.health, self.armor))

    def def_damage(self, person):
        person._atk_damage(self.damage)


class Player(Person):
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)


class Enemy(Person):
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)


class War:
    def __init__(self, person1, person2):
        self.person1 = person1
        self.person2 = person2

    def start(self, person1, person2):
        while person1.health > 0 and person2.health > 0:
            person1.def_damage(person2)
            if person2.health == 0:
                print('{} одержал победу!'.format(person1.name))
                break
            person2.def_damage(person1)
            if person1.health == 0:
                print('{} одержал победу!'.format(person2.name))


player = Player('Яростная буря', 100, random.randrange(1, 20), 40)
enemy = Enemy('Каменный кулак', 110, random.randrange(1, 15), 45)

fight = War(player, enemy)
fight.start(player, enemy)