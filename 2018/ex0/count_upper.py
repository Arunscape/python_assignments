# Arun Woosaree
# Write code that reads from the standard input a string and prints the number of upper-case characters in the string to the standard output.  Hint: there's a method on strings that will tell you if a character is upper or lower case.
# The code should not print anything else to the standard output (i.e., when using input() to get the string from the standard input, do not add a prompt).
#
#
# Example 1:
#
# Input
#
# abc
#
# Output
#
# 0
#
# Example 2:
#
# Input
#
# HelLo
#
# Output
#
# 2
string = input()  # get input
counter = 0

for char in string:  # count uppercase letters
    if char.isupper():
        counter += 1

print(counter)  # display output
