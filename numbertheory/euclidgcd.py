#https://leetcode.com/problems/greatest-common-divisor-of-strings/
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1,l2=len(str1),len(str2)
        if(l1<l2): #Ensure length of str1 is always greater than str2
            return self.gcdOfStrings(str2,str1)
        if(str1[:l2]==str2): #checking str1 is having prefix as str2 or not
            if(l1==l2):
                return str2
            else:
                return self.gcdOfStrings(str2,str1[l2:])
        return ""