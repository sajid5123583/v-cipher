# This module is responsible for reading
# and writing to files


# Given a text file, reads the frequencies of the letters
# and stores them in a dictionary
def read_freq(fileName):
	freqFile = open(str(fileName))
	text = freqFile.read() # text now contains all the characters of freqFile. Wonder if there is a better way
