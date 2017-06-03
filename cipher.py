#Function names follow underscore naming convention
#function arguments are in camelCase

# Returns the square of the argument
def square(num):
	return num ** 2

# Returns the squared root of the argument
def sqrt(num):
	return num ** (1/2.0)

# Returns the standard deviation of the list
def calc_std_dev(list):
	mean = calc_mean(list)
	diffList = diff_with_mean(list, mean)
	return round(sqrt(sum(diffList) / float(len(diffList))))

# Returns a list containing the difference of all elements of the list
# with the mean of the entire list
def diff_with_mean(list, mean):
	diffList = []
	for num in list:
		diff = square(num - mean)
		diffList.append(diff)

	return diffList

# Returns the arithmetic mean of a list
def calc_mean(list):
	if len(list) == 0:
		return 0
	return sum(list) / float(len(list))

# Supposed to return the length of the key of a cipher text
def get_key_length(cipherText):

	print "The length of the cipher text is " + str(len(cipherText))
	shiftList = []
	for shift in range(1, len(cipherText)):
		shiftList.append(shift_compare(cipherText, shift))
	print shiftList	
	std_dev = calc_std_dev(shiftList)
	print "The standard deviation of the list is " + str(std_dev)
	key_len = find_dist_of_bigger_numbers(shiftList, std_dev)
	print "Key length is " + str(key_len)
	return key_len

# Finds the distance between the relatively bigger numbers in the list
def find_dist_of_bigger_numbers(list, threshold):
	dist = 0
	numFound = 0 #number of times we found the bigger number
	for num in list:
		if num > threshold:
			numFound += 1
			if numFound >= 2:
				return dist + 1
			dist = 0
		else:
			dist += 1

	return dist + 1

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
# numbers = map(int, cipherText.split())
# print str(calc_std_dev([55, 15, 13, 12, 45, 16, 19, 14, 53, 18, 14, 12, 63]))
get_key_length(cipherText)


# 0 1 2 3 4 5 len 
# a b c d e f -> cipherText
#   a b c d e 1
#     a b c d 2
#       a b c 3
#         a b 4
#           a 5

# for i in range(shiftLength, totalLength)
# 	compare cipherText[i] and cipherText[i - shiftLength]