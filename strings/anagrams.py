def anagrams(a,b):
    if(sorted(a)==sorted(b)):
        return True
    return False
while True:
    try:
        a,b=map(str,input("Enter a and b:    ").split())
        print(anagrams(a,b))
    except:
        print("invalid input!")
        break