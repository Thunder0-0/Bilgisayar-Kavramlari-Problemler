# -*- coding: utf-8 -*-
'''
İki adet yığın (stack) kullanarak bir çift yönlü sıra (double ended queue) kodlayınız. 
Buna göre sıranın hem başından ekleme ve çıkarma hem de sonundan ekleme ve çıkarma işlemleri yapılabilecektir. 
Önemli bir durum yığınlardan birisinin içinde eleman kalmayınca ve
 sıradaki eleman istenince diğer yığındaki elemanlardan birisinin bu yığına taşınmasıdır.
-----

Create a double ended queue using two stacks.
Accordingly, both insertion and subtraction at the beginning of the row and insertion and subtraction at the end can be performed.
One important situation is that there are no elements left in one of the heaps and
 the next element is to move one of the elements in the other stack to this stack when desired.

 -Translated by Google
 '''

list_end = []

list_head = []

def create_Cluster(number_of_elements_to_add):

    if(number_of_elements_to_add <= 0):
        print('number of elements cannot be negative! \n')
               
    else:
        control0 = 0
        while(control0 < number_of_elements_to_add): 

            list_head.append(int(input('number to add\n:')))
            control0 += 1
        
        for i in range(0, int(len(list_head) / 2)):
            list_end.append(list_head.pop())


def add_To_Head(element_to_add):
    list_head.reverse(); list_head.append(element_to_add); list_head.reverse()

def add_To_End(element_to_add):
     list_end.reverse(); list_end.append(element_to_add); list_end.reverse()

def dell_Head():
    list_head.reverse(); list_head.pop(); list_head.reverse()

def dell_End():
    list_end.reverse(); list_end.pop(); list_end.reverse()


def edit_Lists():
    if(len(list_head) == 0 and len(list_end) > 1):

        for i in range(0, int(len(list_end) / 2)):
            list_head.append(list_end.pop(len(list_end) - 1))
    
    elif(len(list_end) == 0 and len(list_head) > 1):
        for i in range(0, int(len(list_head) / 2)):
            list_end.append(list_head.pop(len(list_head) -1))
        list_end.reverse()

