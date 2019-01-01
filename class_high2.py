#-*- coding:utf-8 -*-
#! usr/bin/python3

class Student(object):
	def __init__(self,name,age,score):
		self._name = name
		self._age = age
		self._score = score

	@property
	def get_score(self):
		return self._score

	def get_age(self):
		return  self._age

	def get_name(self):
		return self._name

	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100')
		self._score = value
