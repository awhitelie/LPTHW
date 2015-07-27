# imports argv variable from sys module
from sys import argv

# assigns input from user upon run to argv
script, filename = argv

# takes inputted filename, opens it, assigns it to variable 'txt'
txt = open(filename)

# prints known filename, reads file 'txt' and prints contents
print "Here's your file %r:" % filename
print txt.read()

# asks user for the filename again, assigns to new variable
print "Type the filename again:"
file_again = raw_input("> ")

# opens file from assigned variable and assigns contents to new variable
txt_again = open(file_again)

# reads and prints contents of txt_again file
print txt_again.read()
