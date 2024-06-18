# Calculating the Sum of Elements in an Array
array=[3, 1, 4, 1, 5, 9]

def sum_array(arr):
    total=0
    for value in arr:
        total+=value
    return total

print(f"The total number of arrays is {sum_array(array)}")