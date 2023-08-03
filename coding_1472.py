"""
the number is positive and top 3

    put in top 3
        the number dropped is neg
            negcount -= 1

the number is neg, top3, there are 0 or 1 negs in top 3

    put in top 3
        negcount += 1
        
the number is neg, top 3, there are 2 negs in top 3
    put in top 3
    drop the highest neg
    
    
-----------------------------------
top 3 positives and negatives

1,2,3

a,b,c

x,y,z


1,a,b

1,2,3

a,b,z

----------------------------------
SOLUTION EXPLANATION 
----------------------------------

The number can only constitute one of two solutions. 
  - Either all three of the largest positive numbers produce the largest product
  - Or the largest two negatives and the largest positive number. The two negatives will cancel eachother out.
  - If the list has no positive numbers, the largest product will be . 
  
The most effective solution envisioned was the following
    1.  loop through the list sorting and dividing the list into three lists 
        containing the 2 largest negative numbers, the largest 3 positive numbers, and the three smallest negative numbers.
    3.  Check if there is at least 1 positive number, multiply top two negatives.
    4.  if there are only negatives, multiple least negatives and return
    5.  Check if there are three positive numbers, multiply top 3 positives.
    6.  return max of product 1 and product 2


"""
import numpy as np

def getLargest3Product(nums):
    if len(nums) < 3:
        # not enough numbers
        return 0
    if len(nums) == 3:
        # the only product that exists
        return np.prod(nums)
    top3pos = []
    top2neg = []
    bot3neg = []
    for n in nums:
        if n < 0: # neg
            if len(top2neg) == 0:
                # list is empty, add elements
                top2neg = [n]
                bot3neg = [n]
            else: # list is non empty, iterate through to place the number
                for i,k in enumerate(top2neg):
                    if k >= n: # if number is larger absolutely than the current top negative number
                        if i == 0: # current top number is largest number, place current number in front
                            top2neg = [n,top2neg[0]]
                            break
                        elif i == 1: # current top number is second largest number, place current number behind the largest number
                            top2neg = [top2neg[0],n]
                            break
                for i,k in enumerate(bot3neg):
                    if k <= n: # if the number is larger than the current bottom negative number
                        if i == 0: #number is new smallest negative
                            bot3neg =  [n] + bot3neg[0:min(len(bot3neg),2)]
                            break
                        elif i == 1: #number is new second largest
                            bot3neg = [bot3neg[0],n,bot3neg[1]]
                            break
                        elif i == 2: #number is the new third largest number
                            bot3neg = bot3neg[0:2] + [n]
                            break
                    elif len(bot3neg) < 3: # still building list
                        bot3neg = bot3neg + [n]
        else: # pos
            if len(top3pos) == 0:
                # list is empty, add element
                top3pos = [n]
            else:# list is non empty, iterate through to place the number
                for i,k in enumerate(top3pos):
                    if k <= n: # if the number is larger than the current top positive number
                        if i == 0: #number is new largest
                            top3pos = [n] + top3pos[0:min(len(top3pos),2)]
                            break
                        elif i == 1: #number is new second largest
                            top3pos = [top3pos[0],n,top3pos[1]]
                            break
                        elif i == 2: #number is the new third largest number
                            top3pos = top3pos[0:2] + [n]
                            break
                    elif len(top3pos) < 3: # still building list
                        top3pos = top3pos + [n]
    print(bot3neg)
    print(top2neg)
    print(top3pos)
    product1 = 0
    if len(top3pos) > 0:
        product1 = top3pos[0] * np.prod(top2neg) # product made of two largest negatives and largest positive
    else:
        return np.prod(bot3neg)
    if len(top3pos) > 2:    
        return max(np.prod(top3pos),product1) # product made of three largest positives
    else: 
        return product1
    
    
t1 = [-10,-10,5,2]
print(getLargest3Product(t1)) # 500

t2 = [-20, 40, -80, 100, 71, 25, 33, -120, 52, 172, -61]
print(getLargest3Product(t2)) # 1,651,200
        
t3 = [10,20,30,40,50,60]    
print(getLargest3Product(t3)) # 120,000

t4 = [-10,-20,-30,-40,-50,-60]
print(getLargest3Product(t4)) # -6,000

t5 = [60,50,40,30,20,10]    
print(getLargest3Product(t5)) # 120,000

t6 = [-10,-20,-30,-40,-50,-60]
print(getLargest3Product(t6)) # -6,000
    