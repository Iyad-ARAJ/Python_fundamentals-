arr = [32,100,22,13,53,43]
def myfunction(arr):
  for i in range (len(arr)-1) :
      min = i
      for j in range(i+1,len(arr)):
          if arr[j] < arr[min]:
              arr[j],arr[min] = arr[min],arr[j]
              print(arr)
print(myfunction(arr))
