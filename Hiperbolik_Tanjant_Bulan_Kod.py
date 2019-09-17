#!/bin/python3

# ((e^2x) -1) / ((e^2x) +1)
#
import math

sonuc = []

def hib_tan(sayi):
	return sonuc.append((((math.e) ** (2 * sayi)) - 1) / (((math.e) ** (2 * sayi)) + 1))


hib_tan(int(input("Sayıyı giriniz: ")))

print(sonuc[0])