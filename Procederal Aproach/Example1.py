# Finding the maximum element in an array
array = [3, 1, 4, 1, 5, 9]
def find_max(arr):
    max_array =arr[0]
    for value in arr:
        if value > max_array:
            max_array = value
    return max_array
print(f"The maximum number in the array is {find_max(array)}")