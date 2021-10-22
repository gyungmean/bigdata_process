#!/usr/bin/python3

print('input two numbers: ')
a = input()
b = input()

try:
	print(float(a) /float(b))
except ZeroDivisionError:
	print('division by zero')

