#!/usr/bin/python3

from LowestPrimeDivisorsGenerator import *
from Power import *

class PrimeFactorsGenerator:
	def __init__(self, n):
		self.__n = int(n)
		self.__primeFactors = None

	def get(self):
		if self.__primeFactors is None:
			self.__primeFactors = self.__get_factors()

		return self.__primeFactors.copy()

	def __get_factors(self):
		n = self.__n
		lowestPrimeDivisors = LowestPrimeDivisorsGenerator(n)

		factors = []
		while n > 1:
			divisor = lowestPrimeDivisors.get(n)
			
			factors.append(Power(divisor,
								 self.__get_exponent(n, divisor)))

			n //= factors[len(factors)-1].value()

		return factors

	def __get_exponent(self, n, divisor):
		cnt = 0
		
		while n % divisor == 0:
			cnt += 1
			n //= divisor

		return cnt
