# Searching for an Element in an Array
array = [3, 1, 4, 1, 5, 9]
target = 5      

def search_element(array,target):
    for i in range(len(array)):
        if array[i]==target:
            return i
    return -1
if search_element(array,target)!=-1:
    print("Element found at index",search_element(array,target))
else:
    print("Element not found")
