from math import log, cos, sin, atan, log10, log2

   
a = 1.5
b = 3.5
h = 0.05
x = a 

while x <= b :

    if x < 2.2:
        result = log10(log(x)+log2(x))
    elif x >= 2.2 and x < 3:
        result = (cos(x)**2)+(cos(x)/sin(x))**(1/4)
    elif x >= 3.5:
        result = atan(1/x)
    print(f"x = {x:.2f}")
    x += h
    x = round(x, 2s)
    print((x))
    