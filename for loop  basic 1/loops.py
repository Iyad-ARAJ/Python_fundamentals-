for i in range(150):
    print(i)

# ===== 2=====
# =============
for i in range(5,1000,5):
    print(i)

# ========3=====
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
# =========4=======
# ------------ 
sum = 0 
for i in range (1,500000,2):
    sum += i 
print(sum)
# =========5========
# count down by 4 ,start from 2018
for i in range(2018, 0, -4):
    print(i)

# =======6======
# ==========      
lowNum = 2
highNum = 9
mult = 3  
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)