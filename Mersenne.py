#!/bin/python3

'''
Mersenne asal sayıları, hem bir Mersenne sayısı, hem de asal sayı olan sayılardır.
Yani n sayısı için Mn = 2^n − 1 işleminin sonucu bir asal sayı ise bu sayıya Mersenne asal sayısı denir.
Yukarıdaki işlemde n = 2 için Mn = 3 olur.
İlk Mersenne asal sayısı 3 tür.
1 3 7 15 
'''


def mersbul(adet):
	KabaListe = []
	MersAsallari = []

	if(adet < 0):
		print("Adet negatif olamaz.")
	else:
		while(len(KabaListe) <= adet):
			for ussu in range(0, adet):
				KabaListe.append((2 ** ussu) - 1)
			break

		for eleman in range(0, (len(KabaListe))):
			for bolen in range(2, KabaListe[eleman] - 1):
				if()




	print(KabaListe, "asdasdasd", MersAsallari)




mersbul(8)
