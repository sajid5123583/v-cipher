#Function names follow underscore naming convention
#function arguments are in camelCase

import read
import calc

cipherText = raw_input("Enter the cipher text: ")
calc.get_key_length(cipherText)


# 0 1 2 3 4 5 len 
# a b c d e f -> cipherText
#   a b c d e 1
#     a b c d 2
#       a b c 3
#         a b 4
#           a 5

# for i in range(shiftLength, totalLength)
# 	compare cipherText[i] and cipherText[i - shiftLength]



# numbers = map(int, cipherText.split())
# print str(calc_std_dev([55, 15, 13, 12, 45, 16, 19, 14, 53, 18, 14, 12, 63]))