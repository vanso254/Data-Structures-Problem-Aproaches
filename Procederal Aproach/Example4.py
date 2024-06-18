#Checking if the array is sorted
array1 = [1, 2, 3, 4, 5]
array2 = [5, 1, 4, 2, 3]

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
print (f"Array 1 is sorted properly: {is_sorted(array1)}")
print (f"Array 2 is sorted properly: {is_sorted(array2)}")