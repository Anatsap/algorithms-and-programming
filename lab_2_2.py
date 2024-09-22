from math import cos

a = 1.1
b = 3.5
h = 0.1
d = 0.001
x = a 
while x <= (b + 1e-8):
    result = 0
    k = 1
    while True:
        value = ((-1)**(k+1)*cos(k*x))/(x+2*k)**3
        if abs(value) <= d:
            break
        k+=1
        result+=value
    print("sum:", result, "x:", x)

    x+=h
        