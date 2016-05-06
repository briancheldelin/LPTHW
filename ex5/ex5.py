name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = ' Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not to heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

inch_to_centimeter = 2.54
pounds_to_kilogram = 0.453592

print "Let's talk about %s, if he were to live in europe." % name
print "He would be %d centimeters tall." % (height * inch_to_centimeter)
print "He would be %r kilograms heavy." % (weight * pounds_to_kilogram)
