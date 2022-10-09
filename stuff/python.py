cars=100
space_in_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_car
average_passengers_per_car=passengers/cars_driven

print ("There are", cars,"cars available.")
print ("there are only",drivers,"drivers available")
print ("there will be",cars_not_driven,"empty cars today")
print ("we can transport",carpool_capacity,"people today")
print ('we have',passengers,'to carpool today')
print ('we need to put about',average_passengers_per_car,'in each cat.')


print ("Hello, World!!")

print ("Mary had a liitle lamb.")
print( "It's fleece was white as %s" % 'snow')
print ("and everywhere that Mary went.")
print ("." *10 #Let's see what that does)
end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

print end1 + end2 + end3 + end4 + end5+ end6,
print end7 + end8+ end9+ end10+ end11+ end12

print ("Hello World")

print ("What's your name?")
name=raw_input()
print ("How old are you?")
age = raw_input()
print ("How tall are you?")
height = raw_input()
print ("How much do you weigh?")
weight = raw_input()

print ("So your name is %r and you're %r years old, %r feet tall and %r kgs heavy" % (name,age,height,weight))


my_name = "sam"
print ("My name is %s." % (my_name))
