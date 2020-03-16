import random
def findp(dot_all):
    dot_in = 0
    control_point = 0
    
    while(control_point < dot_all):
        control_point += 1
        
        x = random.uniform(0,1)
        y = random.uniform(0,1)

        if (1 >= x**2 + y**2):
            dot_in += 1

    return float(4 * dot_in / dot_all)

print(findp(float(input("dot_all: "))))
