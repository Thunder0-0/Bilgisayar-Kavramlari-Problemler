#!/bin/python3

import numpy as np

liste1 = []
#liste2 = []

while(True):
    q = input("Çıkmak istiyorsan (q), devam etmek için (c)")
    
    if (q == "q"):
        print("Kapatılıyor...")
        break
    elif(q == "c"):
        liste1.clear() #Kullanıcı devam ettiğinde eski değerleri sil
        
        try:
        #satırM M --> Mikatrı
            satirM = int(input("İki boyutlu bir matris yaratacağız. \nNe kadar satır olsun:"))
            sutunM = int(input("Ne kadar sutun olsun:"))
        #satır * sutun = eklenecek sayı miktarı
        except(ValueError):
            print("Satır ve sutun değerleri birer sayı olmalı.")
            break
            

        kontrol = 1
        satir = 1
        sutun = 1
        while(kontrol <= satirM * sutunM):
             while(sutun <= sutunM and satir <= satirM ):
                 deger = input("{0}. satir, {1}. sutun:".format(satir,sutun))
                 try:
                     int(deger)
                 except(ValueError):
                     print("Matris elemanları birer sayı olmalıdır.")
                     sutun = sutunM
                     satir = satirM
                     break
                     
                 liste1.append(int(deger))
                 sutun +=1
             sutun = 1
             satir += 1
             kontrol += 1
        try:
            c = np.array(liste1).reshape(satirM,sutunM)
        except(ValueError):
                break
        if(satirM == sutunM):
            print("Matris:\n",c ," \nMatrisin Transpozu:\n" ,c.T ,"\nMatrisin Tersi:\n", c[::-1] ,"\nMatrisin Determinantı: \n", np.linalg.det(c),"\nBoyut:", c.ndim,  "\nEvet, iki boyutlu bir matris elde ettik. Şimdi...\n")
        else:
            print("Matris:\n",c ," \nMatrisin Transpozu:\n" ,c.T ,"\nMatrisin Tersi:\n", c[::-1] ,"\nBoyut:", c.ndim,  "\nEvet, iki boyutlu bir matris elde ettik. Şimdi...\n")

    else:
        print("Geçerli değer girin.")

