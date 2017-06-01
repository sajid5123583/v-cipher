#Function names are in underscore naming
#function arguments are in camelCase

def square(num):
	return num ** 2

def sqrt(num):
	return num ** (1/2.0)

def calc_std_dev(list):
	mean = calc_mean(list)
	diffList = diff_with_mean(list, mean)
	return sqrt(sum(diffList) / float(len(diffList)))

def diff_with_mean(list, mean):
	diffList = []
	for num in list:
		diff = square(num - mean)
		diffList.append(diff)

	return diffList

def calc_mean(list):
	if len(list) == 0:
		return 0
	return sum(list) / float(len(list))

def get_length(cipherText):

	print "The length of the cipher text is " + str(len(cipherText))
	for shift in range(1, len(cipherText)):
		print shift_compare(cipherText, shift)


# Compares the cipherText with a version of it shifted by shiftLength
def shift_compare(cipherText, shiftLength):
	assert(shiftLength <= len(cipherText))
	numMatch = 0
	totalLength = len(cipherText)
	for shiftIndex in range(shiftLength, totalLength):
		if(cipherText[shiftIndex] == cipherText[shiftIndex - shiftLength]):
			# print "{} and {} match".format(cipherText[shiftIndex], cipherText[shiftIndex - shiftLength])
			numMatch += 1

	return numMatch

cipherText = raw_input("Enter the cipher text: ")
numbers = map(int, cipherText.split())
print str(calc_std_dev(cipherText))
# get_length(cipherText)


# 0 1 2 3 4 5 len 
# a b c d e f -> cipherText
#   a b c d e 1
#     a b c d 2
#       a b c 3
#         a b 4
#           a 5

# for i in range(shiftLength, totalLength)
# 	compare cipherText[i] and cipherText[i - shiftLength]