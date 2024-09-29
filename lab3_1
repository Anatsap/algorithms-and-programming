def find_even_index(arr):
    for index in range(len(arr)):
        a = arr[1+index:]
        b = arr[:index]
        if sum(a) == sum(b):
            return index 
    return -1

x = [15, 15, 10, 5, 25, 5, 10]  
index = find_even_index(x)
print(index)
