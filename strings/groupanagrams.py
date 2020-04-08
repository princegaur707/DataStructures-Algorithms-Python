from collections import defaultdict 

def printAnagramsTogether(words): 
	groupedWords = defaultdict(list) 
	for word in words: 
		groupedWords["".join(sorted(word))].append(word)
	for group in groupedWords(): 
		print(" ".join(group))
        
if __name__ == "__main__": 
	arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
	printAnagramsTogether(arr)	 
    print(groupedWords.items())