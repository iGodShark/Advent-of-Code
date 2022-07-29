#get input as array
inputFile = open("input.txt", "r")
strings = inputFile.read().split("\n")
inputFile.close()

#is the string nice (according to requirements)
def isNice(str):
    #the string can't contain either of these combinations of letters
    illegalCombos = ["ab", "cd", "pq", "xy"]
    for illegalCombo in illegalCombos:
        if illegalCombo in str:
            return False
    
    #the string must contain at least 3 vowels
    vowels = list("aeiou")
    vowelCount = 0
    chars = list(str)

    for char in chars:
        if char in vowels:
            vowelCount += 1
    
    if vowelCount < 3:
        return False
    
    #the string must have at least one double string
    for i in range(len(chars) - 1):
        if chars[i] == chars[i+1]:
            return True
    
    return False

niceStrings = 0

for str in strings:
    if (isNice(str)):
        niceStrings += 1

print("Day 1 Solution:", niceStrings, "Nice Strings.")