# =======1======
# ======= countdown =======
def countdown(num):
    arr=[]
    for i in range(5,-1,-1):
        arr.append(i)
    return arr   
count = countdown(5)
print(count)

# ======2=====
# ======print and return======
def myfunction(arr):
    print(arr[0])
    return arr[1]
    
result = myfunction([1,2])

# ======3=====
# ===first plus=====

def first_plus(arr):
    sum = len(arr) + arr[0]
    print(sum)
result = first_plus([1,2,3,4,5])

# ==========4=======
# ==Values Greater than Second==

def values_greater(lst):
    if len(lst) < 2:
        return False
    second = lst[1]
    new_list = []
    for x in lst:
        if x > second:
            new_list.append(x)
    return(new_list)
   

    
result = values_greater([5, 2, 3, 2, 1, 4])
print(result)
print(values_greater([3]))

# ==========5=======
# ==== this length that value=====
def length_and_value(num1,num2):
    newarr = []
    
    
    for x in  range (num1) :
        newarr.append(num2)
    print(newarr)    
    
    
result = length_and_value(4,7)

