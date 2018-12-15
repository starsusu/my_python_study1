# -*- coding:utf-8 -*-
#! usr/bin/python3

class Duck:
    def quack(self):
        print("quaaaaaaa1")


class Bird:
    def quack(self):
        print("quaaaaaaa2")

class Doge:
    def quack(self):
        print("quaaaaaaa3")

def in_the_forest(duck):
    duck.quack()

duck = Duck()
bird = Bird()
doge = Doge()

in_the_forest(doge)



