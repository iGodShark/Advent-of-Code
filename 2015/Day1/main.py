#get input as array
inputFile = open("input.txt", "r")
inputArr = list(inputFile.read())
inputFile.close()

#part 1
values = [1 if char == "(" else -1 for char in inputArr]
total = sum(values)
print("Final floor: " + str(total))

#part 2
runningTotal = 0
for i in range(len(values)):
    runningTotal += values[i]
    if runningTotal == -1:
        print("First time in basement: Character " + str(i + 1))
        break