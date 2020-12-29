#get input as array
inputFile = open("input.txt", "r")
inputArr = list(inputFile.read())
inputFile.close()

#part 1
x = 0
y = 0
housesVisited = [(x,y)]

for direction in inputArr:
    if direction == "<":
        x -= 1
    elif direction == ">":
        x += 1
    elif direction == "^":
        y += 1
    elif direction == "v":
        y -= 1

    newCoordinate = (x,y)

    if (newCoordinate not in housesVisited):
        housesVisited.append(newCoordinate)

print("The number of houses santa visits is: " + str(len(housesVisited)))

#part 2
santaX = 0
santaY = 0
roboSantaX = 0
roboSantaY = 0
housesVisited = [(santaX,santaY)]

for i in range(0, len(inputArr)):
    direction = inputArr[i]

    if i % 2 == 0:
        if direction == "<":
            santaX -= 1
        elif direction == ">":
            santaX += 1
        elif direction == "^":
            santaY += 1
        elif direction == "v":
            santaY -= 1
        
        newCoordinate = (santaX, santaY)
        if (newCoordinate not in housesVisited):
            housesVisited.append(newCoordinate)

    else:
        if direction == "<":
            roboSantaX -= 1
        elif direction == ">":
            roboSantaX += 1
        elif direction == "^":
            roboSantaY += 1
        elif direction == "v":
            roboSantaY -= 1

        newCoordinate = (roboSantaX, roboSantaY)
        if (newCoordinate not in housesVisited):
            housesVisited.append(newCoordinate)

print("The number of houses santa and robo santa visit is: " + str(len(housesVisited)))