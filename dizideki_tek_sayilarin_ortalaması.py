#!/bin/python3
'''
dizideki tek sayıların ortalamasını bulan kod -- find odd numbers in list and find average of them

'''
numbers = []

while(True):
    
    controlPoint1 = True # for check user's want
    if(controlPoint1 == True):
        try:
            x = int(input("Which numder do you want to add to list? "))
        
        except(ValueError):
            print("You can just add numbers!")
            break
        
        numbers.append(x)
        
    controlPoint1 = input("Do you want to continue to adding numbers? (Y/N): ")
    
    if(controlPoint1 == "Y" or controlPoint1 == "y"):
        continue
    
    elif(controlPoint1 =="N" or controlPoint1 =="n"):
        result = 0
        counterOdd = 0
        for i in numbers:
            if(i % 2 != 0):
                result = result + i
                counterOdd = counterOdd + 1 # or you can create another list and add odds into it.
            
            else:
                pass
            
        print(result/counterOdd)
        
        break
    else:
        print("You must enter Yes or No! ")
        break
        