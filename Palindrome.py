# -*- coding: utf-8 -*-

'''list1.split 
list2 = list(list1)
_________

'''


while(True):
    
    try:
        numberId1 = int(input("number?\n: "))
        
    except(ValueError):
        print("You should enter a number!")
        break
    
    copyNum = list(str(numberId1))
    copyNumReverse = copyNum.copy(); copyNumReverse.reverse()
    
    if(copyNum == copyNumReverse):
        print(numberId1,"Yes, this number is a Palindrome!")
    else:
        print(numberId1,"No, this number is not a Palindrome!")