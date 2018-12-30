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

class Student(object):
	name = 'Student'
	# def __init__(self,name):
	# 	self.name = name


if __name__ == '__main__':
	s = Student('bob')
	print(s.name)
	# print(Student.name)
	s.name = 'Michael'
	print(s.name)
	print(Student.name)
	del s.name
	print(s.name)


