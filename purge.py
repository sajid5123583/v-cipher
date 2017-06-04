import sys

fileName = str(sys.argv[1])
toPurge = str(sys.argv[2])
print fileName
print toPurge

file = open(fileName, "r")
lines = file.readlines()
file.close()

newName = "purged_" + fileName
file = open(newName, "w")

for line in lines:
	if line != toPurge:
		file.write(line)

file.close()