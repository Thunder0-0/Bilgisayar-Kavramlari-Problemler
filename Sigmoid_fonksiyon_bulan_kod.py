#!/bin/python3

'''
Verilen bir sayının sigmoid fonksiyonunu veren kodu yazınız.
Sigmoid fonksiyonu (Sigmoid function) basitçe f(x) = 1 / (1+e-x ) olarak yazılabilir.
Sigmoid fonkisyonunun ismi de fonksiyonun kartezyen uzayda çizilmiş halinin andırdığı S harfinden (sigma) gelmektedir.

'''
import math

sonuc = []
def sigmoid_fonk(sayi):
	return sonuc.append(1 / (1 + math.e - sayi))


sigmoid_fonk(int(input("Sayıyı giriniz: ")))
print(sonuc[0])