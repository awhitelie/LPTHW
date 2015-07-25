from sys import argv

script, filename = argv

target = open(filename)

print "Here is your file: "
print "\n"
print target
.read()
print "\n"

print "...aaaand we're done."

target.close()
