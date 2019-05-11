# -*- coding:utf-8 -*-
# ! usr/bin/python3

from types import MethodType


class Student(object):
	# def __init__(self,name,age,score):
	# 	self.__name = name
	# 	self.__age = age
	# 	self.__score = score

	def set_age(self, age):
		self.age = age
		return self.age

	# @property
	# def get_score(self):
	# 	return self.__score
	#
	# def get_age(self):
	# 	return  self.__age
	#
	# def get_name(self):
	# 	return self.__name
	#
	#
	# def set_score(self,value):
	# 	if not isinstance(value,int):
	# 		raise ValueError('score must be an integer')
	# 	if value < 0 or value > 100:
	# 		raise ValueError('score must between 0~100')
	# 	self.__score = value

	__slots__ = ('name', 'age')



s = Student()
s.name = 'Michael'
s.age = 29
# s.score = 89

# def set_age(self, age):
# 	self.age = age
# 	pass
if __name__ == '__main__':
	s2 = Student()
	# s.set_age = MethodType(set_age,s)
	# s2.set_age = MethodType(set_age,s2)

	class GraduateStudent(Student):
		pass
	g = GraduateStudent()
	g.score = 34
	print(g.score)
	s.set_age(25)
	print(s.age)
	s2.set_age(26)
	print(s2.age)
	print(s.age)
