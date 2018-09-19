#tuple is an immutable list


dimensions = (200, 50)													#defining a tuple
print("Original dimensions:")											
for dimension in dimensions:											#looping a tuple
	print(dimension)

#dimensions[0] = 250 is not allowed / error generates since tuple can't be modified. but a touple can be redifined
dimensions = (250, 100)													#defining a tuple
print("New dimensions:")											
for dimension in dimensions:											#looping a tuple
	print(dimension)

