#!/bin/python

def user_input():
	height = float(raw_input("What is your height? "))
	weight = float(raw_input("What is your weight? "))
	unit = raw_input("imperial or metric? ")
	return height, weight, unit

def calculate_bmi(height, weight, unit):
	if unit == "metric":
		bmi = (weight / (height ** 2))
	elif unit == "imperial":
		bmi = 703 * (weight / (height ** 2))
	else:
		print("Did not understand input")
	print("%s bmi = %s" % (unit, bmi))

while True:
	height, weight, unit = user_input()
	if unit.startswith("i"):
		calculate_bmi(height, weight, unit="imperial")
		break
	elif unit.startswith("m"):
		calculate_bmi(height, weight, unit="metric")
		break
	else:
		print("did not understand, try again")
