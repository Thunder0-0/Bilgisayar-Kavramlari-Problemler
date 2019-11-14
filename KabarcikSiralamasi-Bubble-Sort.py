# -*- coding: utf-8 -*-
#!/bin/python3
'''
Karışık sırada verilen bir tam sayı dizisini, 
küçükten büyüğe doğru kabarcık (baloncuk) sıralaması ile (bubble sort) sıralayan kodu yazınız.
means:
take some numbers randomly and list them lower to higher
'''

usersList = []
controlPoint = True
controlPoint1 = "Y" # for list
list2 = []


while(controlPoint == True):
    try:
        usersList.append(int(input("Which number do you want to add? \n: "))) # users input
    except(ValueError):
        print("You should enter a number!")
        break
    
    controlPoint1 = input("Do you want continue to adding numbers? \n(Y/N): ")
    if(controlPoint1 == "y" or controlPoint1 == "Y"):
        pass
    
    elif(controlPoint1 == "N" or controlPoint1 == "n"):
    
        x = 0
        while(x <= len(usersList) - 1):
            for i in range(0, len(usersList) - 1):
                if(usersList[i] > usersList[i + 1]):
                    temp = usersList[i]
                    usersList[i] = usersList[i + 1]
                    usersList[i + 1] = temp
            x = x + 1
        print(usersList)
        break
        
    else:
        print("You should enter Yes or No!")
        break
