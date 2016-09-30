#!/usr/bin/python3

class Power:
	def __init__(self, base, exponent):
		self.base = int(base)
		self.exponent = int(exponent)

	def value(self):
		return self.base ** self.exponent
