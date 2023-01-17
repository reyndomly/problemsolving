"""

The problem is to make a program that print the number of each letter from the string 
Example :

input :
asdfasdasdwaw

output :
    a : 4,
    s : 3,
    d : 3,
    f : 1,
    w : 2

"""

def decompose(word):
    wordDict = {}

    for letter in word :
        try :
            wordDict[letter] += 1
        except KeyError:
            wordDict[letter] = 1
    
    for key, value in wordDict.items():
        print(key+" : "+str(value))

decompose("nainuainaniaieueo")

"""
expected output :

n : 4
a : 4
i : 4
u : 2
e : 2
o : 1

"""
