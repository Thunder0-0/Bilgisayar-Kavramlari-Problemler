import random

def findP(dot_all):
    dot_in, control_point = 0, 0
    
    while(control_point < dot_all):
        control_point += 1
        
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        
        if(1 >= x**2 + y**2):
            dot_in += 1

    return float(4 * dot_in / dot_all)

try:
    print(findP(int(input('dot_all: ))))

except(ValueError):
    print('It should take int')
