import random
def randInt(min= 0 , max = 100):
    if min >= max or max < 0 :
        return False
    
    num = random.random()
    scale_num  = num*(max- min) + min
    return int(scale_num)
    
print(randInt())
print(randInt(max= 50))
print(randInt(min= 50))
print(randInt(min = 50 ,max= 500))
print(randInt(min = 100 ,max= 0))
print(randInt(min = 1001 ,max= 200))

