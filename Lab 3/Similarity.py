# import necessary lib 
# for multiplication
# pip install numpy
import numpy as np 
# for square root
# pip install python-math
import math

def cosine_similarity(x, y):
    # match the index of x and y
    match_with_index = zip(x, y)
    
    product_x_y = [] # Array for the product (dot) of the vectors ‘x’ and ‘y’.
    prod_x_y = [] # temp array to hold the prod
    # list for match index
    list_input = (list(match_with_index))
    
    # step 1 of the computation: x . y = product (dot) of the vectors ‘x’ and ‘y’.
    # example: x[0] * y[0]
    for num in list_input:
        res = np.prod(num)
        prod_x_y.append(res)
        product_x_y = sum(prod_x_y)

    x_power = [] # temp array for the power
    x_sum = [] # temp array for the sum of all power
    x_vector = [] # Square root of the sum 

    # step 2 of the computation: ||x|| length of the the vectors ‘x’.
    # each number will be squared then find the sum, find the square root as the x vector
    for item_x in x:
        sqr_x = item_x ** 2
        x_power.append(sqr_x)
        x_sum = sum(x_power) 
        x_vector = math.sqrt(x_sum)    

    y_power = [] # temp array for the power
    y_sum = [] # temp array for the sum of all power
    y_vector = [] # Square root of the sum 

    # step 3 of the computation: ||y|| length of the the vectors ‘y’.
    # each number will be squared then find the sum, find the square root as the y vector
    for item_y in y:
        sqr_y = item_y ** 2
        y_power.append(sqr_y)
        y_sum = sum(y_power) 
        y_vector = math.sqrt(y_sum)    

    # step 4. substitute all the values to the formula  
    # Cos(x, y) = x . y / ||x|| * ||y||
    cosine = product_x_y / (x_vector * y_vector)
    return round(cosine, 2)


# JEFF JOJER JONES E. CATULAY BSCS 3B