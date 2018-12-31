# -*- coding:utf-8 -*-
#! usr/bin/python3

from types import MethodType
class Student(object):

	def set_age(self,age):
		self.age = age
		return self.age


s = Student()
s.name = 'Michael'


# def set_age(self, age):
# 	self.age = age
# 	pass
if __name__ == '__main__':
	# def set_age(self,age):
	# 	self.age = age
	# 	return
	# s.set_age = MethodType(set_age,s)
	s.set_age(25)
	print(s.age)
	s2 = Student()
	s2.set_age(26)
	print(s2.set_age(87))