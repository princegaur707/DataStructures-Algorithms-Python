from collections import defaultdict

def groupAnagrams(arr):
    dict1=defaultdict(list)
    for i in arr:
        dict1["".join(sorted(i))].append(i)
    print(dict1.values())
groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
