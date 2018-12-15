# -*- coding:utf-8 -*-
#! usr/bin/python3
class Animal(object):
    def run(self):
        print('Animal is running')
        pass
    pass

class Dog(Animal):
    def run(self):
        print("Dog is running")

class Cat(Animal):
    def run(self):
        print("Cat is running")


class Tortoise(Animal):
    def run(self):
        print("Tortoise is running")


def run_twice(animal):
    animal.run()
    animal.run()

class Timer(object):
    def run(self):
        print("start..")

if __name__ == '__main__':
    class Timer(object):
        def run(self):
            print("start..")

    run(animal())

    # run_twice(Tortoise())
    # dog = Dog()
    # dog.run()
    #
    # cat = Cat()
    # cat.run()
    



