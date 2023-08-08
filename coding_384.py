"""
You are given an array of integers representing coin denominations and a total amount of money. 
Write a function to compute the fewest number of coins needed to make up that amount. If it is 
not possible to make that amount, return null.

For example, given an array of [1, 5, 10] and an amount 56, return 7 since we can use 5 dimes, 1 nickel, and 1 penny.

Given an array of [5, 8] and an amount 15, return 3 since we can use 5 5-cent coins.
________________________________________

"""
from math import floor

def findNextValue(coefficients,target,j,maxj):
    """
        Paramaters:
        List: coefficients
        integer: target
        a1x1 + a2x2 + ... + anxn = target
        where x1 are unknowns and a1,a2,...,an are coefficients
        
        j is the maximum value for the unknown k in the system of equations
        
        [
            a1x1 + a2x2 + ... + anxn = target
            x1 + x2 + ... + xn = k
        ]
    Because valid solutions only contain positive integers,
    xi < k is true for all valid solutions
    
    
    """
    if target == 0: # 0 a target of 0 means all x values must be 0
        return 0
    if len(coefficients) == 1: # equation has been reduced to aixi = f, solve for xi
        return target/coefficients[0]
    else:
        x1coeff = coefficients[0]
        newcoefficients = [x - x1coeff for x in coefficients][1:]
        newtarget = target - (j * x1coeff)
        # the above three lines reduce the system using the format
        # (a1 - a1)x1 + (a2 - a1)x2 + ... (an - a1)xn = target - (a1 * k)
        xnvalue = findNextValue(newcoefficients,newtarget,1,j)
        if xnvalue is not None and xnvalue <= j and int(xnvalue) == xnvalue:
            return int(xnvalue)
        if j <= maxj: # value not found, increment j
            return findNextValue(coefficients,target,j + 1,maxj)
        else:
            return None
    
        
        




def solveSystem(coefficients,target,values):
    """
        Solve for xn
        Insert xn into equation to obtain a new equation of the form
        
        [
            a1x1 + a2x2 + ... an-1xn-1 = target - (an * xn)
        ]
        repeat until all xi's are known
        return sum of xi's
        print xi's
        
        
        minimum J is int(target / max(coeff)) because that is base case
        Anything less than max will require more coins and therefore any subcombination
    """
    # precondition: coefficients are sorted least to greatest
    coefficients = [x for x in coefficients if x <= target]
    coefficients = sorted(coefficients)
    newcoefficients = coefficients    
    while len(coefficients) > len(values):
        minj = floor(target/newcoefficients[len(newcoefficients)-1])
        maxj = floor(target/newcoefficients[0])
        # initialize max and minimum k values
        lastx = findNextValue(newcoefficients,target,minj,maxj)
        # solve for xn
        if lastx is None: # no solution found
            return None
        else:
            values = [lastx] + values # add values
            target = target - (newcoefficients[len(newcoefficients)-1] * lastx)
            newcoefficients = newcoefficients[:len(newcoefficients)-1]
            # update and reduce equation
    print(values)
    return int(sum(values))
        
            
        
    
    
    
    
coef = [1,2,5,10,16]
target = 77



values = []

print(solveSystem(coef,target,values))


coef2 = [5,10]
target2 = 14
values2 = []

print(solveSystem(coef2,target2,values2))