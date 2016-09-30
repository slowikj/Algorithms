#!/usr/bin/python3

from PrimeFactorsGenerator import *
from FactorsToNumberConverter import *

class DivisorsGenerator:
	def __init__(self, n):
		self.__n = n
		self.__divisors = None

	def get(self):
		if self.__divisors is None:
			self.__divisors = self.__get_divisors()
			self.__divisors.sort()

		return self.__divisors.copy()

	def __get_divisors(self):
		primeFactors = PrimeFactorsGenerator(self.__n).get()
		divisors = []

		for divisorFactors in self.__get_divisor_factors(primeFactors):
			divisors.append(FactorsToNumberConverter(divisorFactors).get())

		return divisors

	def __get_divisor_factors(self, primeFactors):
		maxFactors = list(primeFactors) + [Power(1, 1)] # adding an artificial element (a sentinel)
		currentFactors = [Power(x.base, 0) for x in maxFactors]

		while currentFactors[len(currentFactors) - 1].exponent == 0:
			for i in range(len(currentFactors)):
				if currentFactors[i].exponent < maxFactors[i].exponent:
					currentFactors[i].exponent += 1
					break
				else:
					currentFactors[i].exponent = 0

			yield currentFactors
