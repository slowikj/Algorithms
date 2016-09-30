#!/usr/bin/python3

class LowestPrimeDivisorsGenerator:
	def __init__(self, n):
		self.__n = int(n)
		self.__lowestPrimeDivisor = None

	def get(self, x):
		if self.__lowestPrimeDivisor is None:
			self.__lowestPrimeDivisor = self.__get_divisors()

		return self.__lowestPrimeDivisor[x]

	def getAll(self):
		return [self.get(x) for x in range(0, self.__n + 1)]

	def __get_divisors(self):
		divisors = self.__initial_divisors()

		is_prime = lambda x: divisors[x] == x

		for x in range(2, self.__n + 1):
			if is_prime(x):
				self.__set_divisor(x, divisors)

		return divisors

	def __initial_divisors(self):
		return list(range(self.__n + 1))

	def __set_divisor(self, x, divisors):
		j = x * x
		
		while j < len(divisors):
			divisors[j] = min(divisors[j], x)

			j += x
