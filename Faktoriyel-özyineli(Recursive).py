#!/bin/python3
'''
Ozyineli Recursive
f(x) =  x * f(x-1)
123456789
3 2 1 0 0 

Fak(0) = 1
'''

def Fak(x):
    if(x == 1 or 0):
        return 1
        
    return x * Fak(x-1)

hataKontrol = False

while(True):
    if(hataKontrol == False):
        q = input("Devam etmek istiyor musunuz? (E/H)")
    elif(hataKontrol == True):
        q = ("E")
        hataKontrol = False
        
    if(q == "H"):
        break
    
    elif(q == "E"):
        try:
            print("Sonuç: ",Fak(int(input("Faktoriyelini almak istediğiniz sayıyı girin: "))))
        
        except(ValueError):
            print("Bir sayı girmelisin")
            hataKontrol = True
    else:
        print("Geçerli bir değer işlem girin.")

