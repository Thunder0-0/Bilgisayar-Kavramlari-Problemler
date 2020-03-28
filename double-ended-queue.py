#!/bin/python3

"""
İki adet yığın (stack) kullanarak bir çift yönlü sıra (double ended queue) kodlayınız. Buna göre sıranın hem başından ekleme ve çıkarma hem de sonundan ekleme ve çıkarma işlemleri yapılabilecektir. Önemli bir durum yığınlardan birisinin içinde eleman kalmayınca ve sıradaki eleman istenince diğer yığındaki elemanlardan birisinin bu yığına taşınmasıdır.

ekle / çıkar baş

ekle / çıkar son

listeleri düzenle

1,2,3,4,5 --head
10,9,8,7,6 --end
"""

def listAdd(listEnd, listHead, number, point = 1):
    if(point == 1):
        listEnd[:0] = [number]

    elif(point == 0):
        listHead[:0] = [number]
    
    else:
        print('Hata --List Add')
    

def listDel(listEnd, listHead, point = 1):
    if(point == 1):
        listEnd.remove(listEnd[0])

    elif(point == 0):
        listHead.remove(listHead[0])

    else:
        print('Hata --list Dell')
        

def listEdit(list_empty, list_full):
    for sayi in range(0,int(len(list_full)/2)):
            list_empty.append(list_full.pop())


def main(listHead, listEnd):
    while(1):
        if(len(listHead) == 0):
            listEdit(listHead, listEnd)
        
        elif(len(listEnd) == 0):
            listEdit(listEnd, listHead)

        else:
            print('list Head: ',listHead, '\nlist End: ', listEnd)
            operation = int(input('Add --> 1\n Dell --> 2\nBreak --> 3\n: '))
            if(operation == 1):
                listAdd(listEnd, listHead, int(input('number: ')), int(input('Head:0 End:1: ')))

            elif(operation == 2):
                listDel(listEnd, listHead, int(input('Head:0 End:1: ')))
    
            elif(operation == 3):
                break

            else:
                print('Hata --main')


if(__name__ == '__main__'):
    list_head = [1,2,3,4,5]
    list_end = [10,9,8,7,6]

    main(list_head, list_end)


