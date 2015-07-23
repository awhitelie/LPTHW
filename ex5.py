name = 'Christopher Z. Bear'
age = 27 # not a lie
height = 76 # inches
weight = 230 # lbs
weight_kg = weight / 2.2
height_cm = height * 2.54
eyes = 'Hazel'
teeth = 'White'
hair = 'Blonde'



print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d" % (
    age, height, weight, age + height + weight
    )

print "For what it's worth, his height of %d in inches is %d in cm." % (height, height_cm)
print "...and his weight of %d lbs is %d kg." % (weight, weight_kg)
