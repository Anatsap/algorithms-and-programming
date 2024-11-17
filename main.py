import math

matrix = [
    [2, 0, 33, -1, -2],
    [78, 7, -4, -3, 11],
    [-2, -7, -1, -9, 0],
    [13, 61, 60, 42, -10],
    [1, 0, 4, 0, 16],
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

selectionSort(matrix)

res =[]
for i in range(0,len(matrix)):
    s = 0
    for j in range(0,len(matrix)):
        s += matrix[i][j]
    res.append(s)


def main():
    for row in matrix:
        print(row)
    print("The Summation of each index list is : " + str(res))
    geometric_mean = math.sqrt(res[0]*res[1]*res[2]*res[3]*res[4])
    print("Geometric mean = " + str(geometric_mean))

if __name__ == "__main__":
    main()

