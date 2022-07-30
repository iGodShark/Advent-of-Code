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

# Day 1
niceStrings = 0

for str in strings:
    if (isNice(str)):
        niceStrings += 1

print("Day 1 Solution:", niceStrings, "Nice Strings.")

# is the string nice day2?
def isNiceDay2(str):
    # must contain a 3-digit palindrome
    # and contain 2 pairs of 2 characters without overlapping
    containsPalindrome = False
    for i in range(len(str) - 2):
        if str[i] == str[i+2]:
            containsPalindrome = True
            break
    
    if not containsPalindrome:
        return False
    
    # must contain 2 pairs of 2 characters without overlapping
    for i in range(len(str) - 3):
        strPair = str[i] + str[i+1]
        for j in range(i + 2, len(str) - 1):
            if strPair == str[j] + str[j+1]:
                return True
    
    return False

# Day 2
niceStringsDay2 = 0

for str in strings:
    if (isNiceDay2(str)):
        niceStringsDay2 += 1

print("Day 2 Solution:", niceStringsDay2, "Nice Strings.")