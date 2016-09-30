#!/usr/bin/python3

class LowestPrimeDivisorsGenerator:
	def __init__(self, n):
		self.__n = int(n)
		self.__lowestPrimeDivisors = None

	def get(self, x):
		if self.__lowestPrimeDivisors is None:
			self.__lowestPrimeDivisors = self.__get_lowest_divisors()

		return self.__lowestPrimeDivisors[x]

	def getAll(self):
		return [self.get(x) for x in range(0, self.__n + 1)]

	def __get_lowest_divisors(self):
		res = LowestPrimeDivisorsGenerator.__Divisors(self.__n)
		is_prime = lambda x: res.get(x) == x

		for x in range(2, self.__n + 1):
			if is_prime(x):
				res.set_divisor(x)

		return res.getAll()

	class __Divisors:
		def __init__(self, n):
			self.__n = int(n)
			self.__divisors = self.__get_initial_divisors()

		def __get_initial_divisors(self):
			return list(range(self.__n + 1))

		def set_divisor(self, x):
			j = x * x
			
			while j < len(self.__divisors):
				self.__divisors[j] = min(self.__divisors[j], x)
				j += x

		def getAll(self):
			return self.__divisors

		def get(self, x):
			return self.__divisors[x]


	
	
