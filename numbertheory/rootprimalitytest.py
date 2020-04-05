#T.C O(sqrt(n)) 
from math import floor,ceil,sqrt
def checkprime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    for i in range(5,ceil(sqrt(n))+1,6):
        if n%i == 0 or n%(i+2)==0:
            return False
    return True

while True:
    try:
        n = int(input("Enter number:"))
        print(checkprime(n))
    except:
        print("Invalid input!")
        break

