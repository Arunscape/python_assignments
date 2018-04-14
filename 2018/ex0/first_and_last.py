# Arun Woosaree
# Write code that reads from the standard input a string of length at least one and prints the first and last characters of the string to the standard output.
#
# The code should not print anything else to the standard output (i.e., when using input() to get the string from the standard input, do not add a prompt).
#
# You will need to submit your code separately on the code submission page.
#
# Example 1:
#
# Input
#
# abc
#
# Output
#
# ac
#
# Example 2:
#
# Input
#
# Hello
#
# Output
#
# Ho
word = input()  # input

print(word[0] + word[-1])  # print first and last character
