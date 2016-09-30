#!/usr/bin/python3

class FactorsToNumberConverter:
	def __init__(self, factors):
		self.__factors = factors
		self.__value = None
	
	def get(self):
		if self.__value is None:
			self.__value = self.__get_number()

		return self.__value
	
	def __get_number(self):
		res = 1
		for power in self.__factors:
			res *= power.value()

		return res
