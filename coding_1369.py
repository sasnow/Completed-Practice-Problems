"""
Given a string of digits, generate all possible valid IP address combinations.
IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255. 
Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.
For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].


brute force approach

place 3 dots in the string all combinations
filter for valid ip

x='00005'
0.0.0.05
00.0.0.5
0.00.0.5
0.0.00.5

x='123456'
max size = 3
1.2.34.56
    steps
        first number use 1 digit good
            three spaces remaining
                remaining digits less than 10
                    next digit is non zero
            
        second number use 1 digit good
            two spaces remaining
                remaining digits less than 7
                    next digit is non zero
        third number use 1 digit no good
            1 space remaining.
                remaining digits less than 4
                    remaining digits equal 3
                        remaining number is > 255
        third number use 2 digits
            1 space remaining
                remaining digits less than 4
                    remaining digits less than 3
                        next digit is non zero
        fourth number use 2 digits
            third number use 3 digits
                number is not valid
1.23.4.56
1.23.45.6
    steps
        first number use 1 digit good
            three spaces remaining
                remaining digits less than 10
                    next digit is non zero
        second number use 2 digits
            two spaces remaining
                remaining digits less than 7 and greater than 1
                    next digit is non zero
        third number use 1 digit
            1 space remaining
                remaining digits is less than 4
                    remaining digits is less than 3 and greater than 0
                        next digit is non zero
        fourth number use 2 digits
            third number 2 digits
                1 space remaining
                    remaining digits is less than 4
                        remaining digits is less than 3
                            next digit is non zero or is length 1
            fourth number use 1 digit
1.234.5.6
    steps
        first number use 1 digit good
            three spaces remaining
                remaining digits less than 10
                    next digit is non zero
        second number use 3 digits
            two spaces remaining
                remaining digits less than 7 and greater than 1
                    next digit is non zero
        third number use 1 digit
            
         
"""


x = '0000' # becomes 0.0.0.0
x = '255255255255'  # becomes 255.255.255.255
x = '123412046' # 12.34.120.46 or 123.4.120.46 or 123.41.20.46 or 123.41.204.6 or


class IPString:
    def __init__(self,nums):
        self.workingstring = nums
        self.firstvalue = None
        self.secondvalue = None
        self.thirdvalue = None
        self.fourthvalue = None
        self.started = False
        
    def setvalue(self,position,length):
        """
            Extracts the new value from the string and determines if the value will be valid
            Valid values must be equal to the argument length, less than or equal to 255 and cannot start with 0 unless the length is 0
            If valid, returns true to indicate to proceed and removes that portion from the initial string value
        """
        newvalue = self.workingstring[:length]
        testremaining = self.workingstring[length:]
        if self.validremaining(testremaining, position) and self.validvalue(newvalue) and len(newvalue) == length:
            if position == 1:
                self.firstvalue = newvalue
            elif position == 2:
                self.secondvalue = newvalue
            elif position == 3:
                self.thirdvalue = newvalue
            elif position == 4:
                self.fourthvalue = newvalue
            else:
                print("invalid position")
                return False
            self.workingstring = testremaining
            return True
        else:
            return False

    def resetvalue(self,position):
        """
            Resets the placeholder value for that position and 
            updates the working string by adding back the reset value
        """
        if position == 1:
            self.workingstring = self.firstvalue + self.workingstring
            self.firstvalue = None
        elif position == 2:
            self.workingstring = self.secondvalue + self.workingstring
            self.secondvalue = None
        elif position == 3:
            self.workingstring = self.thirdvalue + self.workingstring
            self.thirdvalue = None
        elif position == 4:
            self.workingstring = self.fourthvalue + self.workingstring
            self.fourthvalue = None
        else:
            print("invalid position")
            return False
            
    def validvalue(self, teststring):
        """
            tests conditions for value assignment
        """
        if len(teststring) == 0:
            return False
        if int(teststring) > 255:
            return False
        if teststring[0] == '0' and len(teststring) > 1:
            return False
        return True
         
          
    def validremaining(self, teststring, position):
        """
            tests conditions for value assignment based there being
                enough remaining digits to fill remaining spaces and 
                and enough remaining spaces to handle all remaining digits
        """
        remaininglimit = 13 - (position * 3)
        remainingmin = 3 - position
        return len(teststring) < remaininglimit and len(teststring) > remainingmin
         
    def getip(self):
        """
            used for debug
        """
        return [self.firstvalue,self.secondvalue,self.thirdvalue,self.fourthvalue]
        
    def __str__(self):
        return ".".join([str(self.firstvalue),str(self.secondvalue),str(self.thirdvalue),str(self.fourthvalue)])
        
#---------------------------------------------------------------------------------------------------        

def parseIPs(workingip, lofips, position):
    if position == 5:
        # and ip has been generated
        lofips.append(workingip.getip())
        print("fully reset or position end")
        print(workingip)
        print("Position: " + str(position))
        print(lofips)
        print("--------------------------------------")
    elif position > 0:
        workinglength = 3
        while workinglength > 0:
            print("Length: " + str(workinglength))
            print(workingip)
            print("Position: " + str(position))
            # check if the value is valid
            valid = workingip.setvalue(position,workinglength)
            print("Valid: " + str(valid))
            print("--------------------------------------")
            if valid:
                # move to the next position
                parseIPs(workingip, lofips, position + 1)
            # check less digits for the value
            workinglength -= 1
    # reset the prior position before moving to it
    workingip.resetvalue(position - 1)
        

def chklen(nums):
    return len(nums) > 3 and len(nums) < 13

nums = '2542540123'
nums = '123412046'

if not chklen(nums):
    print("too small or too big")
elif len(nums) == 4:
    print("easy")
    print(".".join([x for x in nums]))
else: 
    IPgenerator = IPString(nums)
    ListofIPs = []   
   
    parseIPs(IPgenerator,ListofIPs,1)
    print(ListofIPs)


    
    
    