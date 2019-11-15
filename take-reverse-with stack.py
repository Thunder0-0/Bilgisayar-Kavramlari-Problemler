# -*- coding: utf-8 -*-
'''
___


____

'''
controlPoint1 = "Y"
list1 = []
list2 = []

while(True):
    
    
    if(True):    
        try:
            tempNum = int(input("Number\n: "))
            
        except(ValueError):
            print("You should enter a number!")
            break
        
        list1.append(tempNum)
        
    controlPoint1 = input("Do you want continue to adding numbers? (Y/N) \n:")
        
    if(controlPoint1 == "Y" or controlPoint1 == "y"):
        continue
    
    elif(controlPoint1 == "N" or controlPoint1 == "n"):
        list1Copy = list1.copy()
        
        x = 0
        while(x <= len(list1)):
            list2.append(list1.pop())
            x =+1
            
        print("Original list: ", list1Copy, "\n Reversed list: ", list2)
        break
        
    else:
        print("You should enter available option like Yes or No!")
        break
