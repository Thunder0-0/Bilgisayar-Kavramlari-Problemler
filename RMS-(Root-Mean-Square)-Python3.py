#!/bin/python3

# RMS(Root(Karekoku)-Mean(Ortalama)-Square(Karesi)) <--

sayilar_liste = []
def RMS_sayilar():
	eklemeistegi = True
	while(eklemeistegi == True):
		sayilar_liste.append(int(input("Eklemek istediğiniz sayı: ")))
		eklemeistegi_kontrol = int(input("Ekleme yapmaya devam etmek istiyor musunuz? (1-0)"))
		if(eklemeistegi_kontrol == True):
			continue
		else:
			return sayilar_liste
			return eklemeistegi == False


sayilar_kare = []
def RMS_kare(): # pow kullanılabilirdi, ama fonksiyon yerine matematik işlemi daha verimli çalışır
	# eleman sayısı = len(sayilar_liste)
	for eleman in range(0, len(sayilar_liste), +1):
		sayilar_kare.append(sayilar_liste[eleman] ** 2)
	return sayilar_kare


ortalama = []
def RMS_ortalama():
	toplam = 0
	for eleman in range(0, len(sayilar_kare)):
		toplam += sayilar_kare[eleman] # sum kullanılabilir
	ortalama_int1 = (toplam / len(sayilar_kare))
	ortalama.append(ortalama_int1)
	return ortalama

karekok = []
def RMS_karekok():
	karekok.append(round((float(float(ortalama[0] ** 0.5))) ,2))
	return karekok


RMS_sayilar()
RMS_kare()
RMS_ortalama()
RMS_karekok()

print(sayilar_liste, sayilar_kare, ortalama, karekok)