matrix = [
    [2, 0, 33, -1, -2],
    [78, 7, -4, -3, 11],
    [-2, -7, -1, -9, 0],
    [13, 61, 60, 42, -10],
    [1, 0, 4, 0, 16],
    [6, 7, 8, 2, 6]
]

def selectionSort(array2d):
    
    for col in range(len(array2d[0])):
        
        n_col = len(array2d)

    

        for step in range(n_col):
            min_idx = step

            for i in range(step + 1, n_col):
            
                if array2d[i][col] < array2d[min_idx][col]:
                    min_idx = i
            
            (array2d[step][col], array2d[min_idx][col]) = (array2d[min_idx][col], array2d[step][col])

# selectionSort(matrix)
# print(matrix)
a = 5
b = 30
a, b = b, a
print(a, b)