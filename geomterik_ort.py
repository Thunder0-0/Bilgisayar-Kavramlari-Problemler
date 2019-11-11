#!/bin/python3
'''
Geometrik ortalama bulan kod/ Code for geometric average find

(x1 . x2 . x3 ... xn)1/n - way to find geometric average
_______________
sayilar = list of numbers
kontrol4 = for check. if user wants continue s/he must return E or e, if  s/he dont want continue, s/he must return H or h
 sonuc = result of this geometric average 
sonuc_raw = just multiply numbers of list

line 27 Eklemek istedigin sayi:                            ------means : which number do you want to add?
line 30 Bir sayi eklemelisin!:                             ------means : you must add a number.
line 35 Sayi eklemeye devam etmek istiyor musunuz? (E/H)\n -----means: Do you want to add other numbers? E = Yes, H = No
line 44 sayilar, "'in geometrik ortalaması:                -----means: geomtetric average of number is, result(sonuc)
line 47 print("Doğru kontrol değerini girmelisin!"          -----means: you must enter one of them(E or H)
_______________

'''

sayilar = []

while(True):
    kontrol4 = "E"
    if(kontrol4 == "E" or "e"):
        try:
            sayi1 = int(input("Eklemek istedigin sayi: "))

        except(ValueError):
            print("Bir sayi eklemelisin!")
            break
        
        sayilar.append(sayi1)
            
    kontrol4 = input("Sayi eklemeye devam etmek istiyor musunuz? (E/H)\n")
    if(kontrol4 == "E" or kontrol4 == "e"):
        continue
    elif(kontrol4 == "H" or kontrol4 == "h"):
        sonuc = 0
        sonuc_raw = 1
        for x in sayilar:
            sonuc_raw = sonuc_raw * x
        sonuc = (sonuc_raw) ** (1/len(sayilar))
        print(sayilar, "'in geometrik ortalaması: ",round(sonuc,2))
        break
    else:
        print("Doğru kontrol değerini girmelisin!")
        break

