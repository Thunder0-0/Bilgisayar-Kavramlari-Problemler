#!/bin/python3

'''
x       y
carpan carpilan
   3  x   5
   5  5  5 

'''

def func(carpan, carpilan):
#    return carpilan + func((carpan - 1), carpilan)
    sonuc = 0
    if(carpan == 0):
        return sonuc
    else:
        return carpilan + func((carpan - 1), carpilan)

print(func(int(input("Carpan: ")),int(input("Carpilan "))))
