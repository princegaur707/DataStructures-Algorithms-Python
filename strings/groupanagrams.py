from collections import defaultdict

def groupAnagrams(arr):
    dict1=defaultdict(list)
    for i in arr:
        dict1["".join(sorted(i))].append(i)
        print(dict1.items())
    print("Here comes the final: ")
    for i,j in dict1.items():
        print(i,j)
groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])