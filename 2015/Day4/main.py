import hashlib

keyPrefix = "yzbqklnj"

# part 1

i = 0
hash = str()

while not (hash.startswith("00000")):
    i += 1
    hash = hashlib.md5((keyPrefix + str(i)).encode()).hexdigest()

print(i)

# part 2

i = 0
hash = str()

while not (hash.startswith("000000")):
    i += 1
    hash = hashlib.md5((keyPrefix + str(i)).encode()).hexdigest()

print(i)