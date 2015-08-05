
def make_list(items):
    """Takes a number, makes a list of the range, prints and returns"""
    list = [ ]
    i = 0
    while i < items:
        print "At the top i is %d" % i
        list.append(i)
        i += 1
        print "Numbers now: ", list
        print "At the bottom i is %d" % i



print "Pick an number and I'll pack it up: "
items = raw_input("> ")

make_list(items)

numbers = list



# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)
#
#     i += 1
#
#     print "Numbers now :", numbers
#     print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
