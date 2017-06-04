# This module is responsible for reading
# and writing to files


# Given a text file, reads the frequencies of the letters
# and stores them in a dictionary

# In a list, finds all toFind and replaces them with replaceWith
def purge(list, toFind, replaceWith):
	length = len(list)
	for i in range(0, length):
		list[i] = list[i].replace(toFind, replaceWith)

def read_freq(fileName):
	freqFile = open(str(fileName), "r")
	lines = freqFile.readlines() # text now contains all the characters of freqFile. Wonder if there is a better way
	
	freqTable = {}

	purge(lines, '\n', '')
	# print lines
	for line in lines:
		pair = line.split(" \t") # the alpha-freq pair
		freqTable[pair[0]] = float(pair[1])


	print freqTable	
	return freqTable

def read_cipher_text():
	cipherText = raw_input("Enter the cipher text: ")
	cipherText = cipherText.replace(' ', '')
	cipherText = cipherText.upper()

	return cipherText

# read_freq('freq.txt') # For testing purposes