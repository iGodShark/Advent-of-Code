#get input
inputFile = open("input.txt", "r")
inputArr = inputFile.read().split("\n")
inputFile.close()

#part 1
dimensionsMatrix = [[int(value) for value in line.split("x")] for line in inputArr]
areasNeeded = list()
for present in dimensionsMatrix:
    area = int()
    indexOfLargest = present.index(max(present))
    for i in range(len(present)):
        for j in range(len(present)):
            if i != j:
                area += present[i] * present[j]
                if i != indexOfLargest and j != indexOfLargest and i > j:
                    area += present[i] * present[j]
    areasNeeded.append(area)

print("Total area of wrapping paper needed: " + str(sum(areasNeeded)))

#part 2
ribbonNeeded = int()
for present in dimensionsMatrix:
    indexOfLargest = present.index(max(present))
    perimeter = int()
    volume = 1
    for i in range(len(present)):
        volume *= present[i]
        for j in range(len(present)):
            if i != indexOfLargest and j != indexOfLargest and i != j:
                perimeter = 2 * (present[i] + present[j])
                break
    ribbonNeeded += perimeter + volume

print("Total amount of ribbon needed: " + str(ribbonNeeded))