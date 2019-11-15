# -*- coding: utf-8 -*-

selectedNumberReversed = []

while(True):
    
    try:
        number = int(input("Number: " ))
    
    except(ValueError):
        print("You should enter a number!")
        break
    
    selectedNumberCopy = list(str(number))
    selectedNumber = selectedNumberCopy.copy()

    for i in range(len(selectedNumber)):
        selectedNumberReversed.append(selectedNumberCopy.pop())
        
    if(selectedNumber == selectedNumberReversed):
        print(number, "It is palindrome!")
        break
    
    else:
        print(number, "It is Not palindrome!")
        break    
    
