def print_result(func):
    def wrap(*args, **kwargs):
        value = func(*args, **kwargs)
        print(f"Method '{func.__name__}' output: {value}")
    return wrap
    


class Matrix:
    def __init__(self, data):
        self.data = data

    @print_result
    def sort(self):  

        for col in range(len(self.data[0])):  
            n_col = len(self.data)

            for step in range(n_col):
                min_idx = step

                for i in range(step + 1, n_col):
                    if self.data[i][col] < self.data[min_idx][col]:
                        min_idx = i
                        
                (self.data[step][col], self.data[min_idx][col]) = (self.data[min_idx][col], self.data[step][col])
        return self


    @print_result
    def adding(self, other: "Matrix"):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions for addition.")
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))])

    def __str__(self):
        return str(self.data)

    @print_result
    def calculate_geometric_mean(self):
        res = 1
        for i in range(0,len(self.data)):
            s = 0
            for j in range(0,len(self.data[0])):
                s += self.data[i][j]
            res *= s 
        res = (res)**(1/len(self.data))
        return res
    
if __name__ == "__main__":
    matrix1 = Matrix([
        [2, 0, 33, -1, -2],
        [78, 7, -4, -3, 11],
        [-2, -7, -1, -9, 0],
        [13, 61, 60, 42, -10],
        [1, 0, 4, 0, 16],
        
    ])
    matrix2 = Matrix([
        [8, 9, 33, -1, -2],
        [51, 7, -2, -5, 11],
        [-5, -7, -1, -9, 0],
        [18, 55, 43, 42, -10],
        [80, 0, 4, 1, 7]
    ])

    matrix1.sort()
    matrix2.sort()

    matrix1.calculate_geometric_mean()

    result_adding = matrix1.adding(matrix2)
