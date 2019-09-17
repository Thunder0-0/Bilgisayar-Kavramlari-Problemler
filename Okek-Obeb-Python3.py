#!/bin/python3

#Okek-Obeb Bulan kod
##
# Ekok = a * b / ebob(a,b)
# Ebobu bulmak daha kolay.
#
# 

kucuksayi = 0
i = 1
ebob = 1

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

if(sayi1 >= sayi2):
	kucuksayi = sayi2
else:
	kucuksayi = sayi1


while(i <= kucuksayi):
	if((sayi1 % i == 0) and (sayi2 % i == 0)):
		if(ebob < i):
			ebob = i

	i += 1


print("Ebob : {}".format(ebob))
print("Ekok : {}".format(sayi1 * sayi2 / ebob))