def ispoweroftwo(n):
    return n and (not(n & (n-1)))

while True:
    try:
        n = int(input("Enter number:    "))
        print(ispoweroftwo(n))
    except:
        print("Invalid input!")
        break
