 # =====1=====
# ===biggie size====
def positive(arr):
    for x in range  (len(arr)):
        
        if arr[x] > 0 :
            arr[x] = "big"
    return arr
    
result = positive([-1, 3, 5, -5])
print(result)
#  ======2=====
#  ===count positive====
def positivevalues(arr):
    count = 0 
    for x in range(len(arr)):
        if arr[x] > 0 :
            count += 1 
    arr[len(arr)-1] = count
    return arr
            
result = positivevalues([-1,1,1,1])
result2 = positivevalues([1,6,-4,-2,-7,-2])
print(result)
print(result2)

# =====3====
# ===sum total===
def sum_total(arr):
     sum = 0 
     for x in arr:
         sum += x
     return sum
    

result = sum_total([1,2,3,4])
print(result)

# ====4====
# ===average ===

def sum_total(arr):
     sum = 0 
     for x in arr:
         sum += x
     return sum/len(arr)
    

result = sum_total([1,2,3,4])
print(result)

# ===5====
# =======
def myfunction(arr):
    return len(arr)

print(myfunction([37,2,1,-9]))

# =====6====
# =======minimum

def myfunction(arr):
    if len(arr) == 0 :
        return False
    min = arr[0]
    for x in range (len(arr)) :
        if arr[x] < min :
            min = arr[x]
    return min
    
    

result = myfunction([37,2,1,-9])
result1 = myfunction([])
print(result)
print(result1)

# ====7=====
# === max====
def myfunction(arr):
    if len(arr) == 0:
        return False
    max = arr[0]
    for x in arr:
        if x > max:
            max = x
    return max
result = myfunction([37,2,1,-9])
result2 = myfunction([])
print(result)
print(result2)

# ====8====
# ==ulitmate analysis

def myfunction(arr):
        sum= 0
        min = arr[0]
        max = arr[0]
        
        for x in range(len(arr)):
            if arr[x] < min:
                min = arr[x]
            if arr[x] > max:
                max = arr[x]
            sum = sum + arr[x]
            avg = sum / len(arr)
            length = len(arr)
        
        result={
            'sum':sum,
            'max':max,
            'min':min,
            'avg':avg,
            'length':length
        }
        return result
    
result = myfunction([37,2,1,-9])
print(result)
    
# =====9=====
# ====reversed====

# def myfunction(arr):
#     for i in range(len(arr)-1):
#         arr.insert(i, arr.pop())
        
#         return arr
# result = (myfunction([37,2,1,-9]))
# #step====  arr=[::-1]
# print(result)
def myfunction(arr):
    for i in range (len(arr)):
        n = len(arr)
        temp = arr[i]
        arr[i]= arr[n-i-1]
        arr[n-i-1] = temp
        print(arr)
        
print(myfunction([37,2,1,-9]))


