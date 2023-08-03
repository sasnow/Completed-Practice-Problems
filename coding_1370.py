"""
Given a string which we can delete at most k, return whether you can make a palindrome.
For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.


"""
from math import floor


def isPalindrome(text):
    """
        Simple function to test if the string is a palindrome
    """
    tlen = len(text) # requires different logic for strings of even and odd lengths
    if tlen % 2 == 0: # even length
        firsthalf = text[0:int(tlen/2)]
        secondhalf = text[int(tlen/2):tlen]
        return firsthalf == secondhalf[::-1]
    else: # odd length
        firsthalf = text[0:floor(tlen/2)]
        secondhalf = text[floor(tlen/2) + 1:tlen]
        return firsthalf == secondhalf[::-1]


def canMakePD(text,k):
    tlen = len(text)
    if tlen <= 1:
        ## successfully found matches until all or all but 1 character remains
        return True
    elif k == 0:
        ## eliminated max letters. check if remainder is palindrome
        return isPalindrome(text)
    else:
        lc = 1
        while lc*2 < tlen + 1:
            check2 = False
            if text[0:lc] == text[tlen - lc:tlen]:
                # edges match strip and recur
                print('1,1')
                newtext = text[lc:tlen-lc]
                return canMakePD(newtext,k)
            if text[1:lc + 1] == text[tlen - lc:tlen]:
                # matches in left side
                # strip left 2 and right 1 and recur k - 1
                print('2,1')
                newtext = text[lc + 1:tlen-lc]
                check2 = canMakePD(newtext,k-lc)
            if not check2 and text[0:lc] == text[tlen - lc - 1:tlen - lc]:
                # matches in right side
                # strip left 1 and right 2 and recur k - 1
                print('1,2')
                newtext = text[lc:tlen - lc - 1]
                return canMakePD(newtext,k-lc)
            if check2:
                # example - racajra
                # left 2, right 1 will match but will result
                # newtext = cajr which will fail
                # matching left 1, right 2 results in acaj which will succeed
                return check2
            if lc * 2 <= k and text[1:lc + 1] == text[tlen - lc - 1:tlen - lc]:
                # can drop 2 * current loop letters
                # matches in both sides
                # strip left 2 and right 2
                # recur k - 2
                print('2,2')
                newtext = text[lc + 1:tlen - lc - 1]
                return canMakePD(newtext,k-(lc*2))
            else:
                # no matches found incr loop counter
                lc += 1
        return isPalindrome(text) and (check1 or check2 or check3 or check4)
                
                
                
#print(isPalindrome('robot'))

test = 'waterrfetawx'
print(canMakePD(test,2))