magicians = ['alice', 'david', 'carolina']						
for magician in magicians:												#using a for loop
	print(magician+"\n")
numbers=list(range(1,8))												#range function
print(numbers)
even_nos=list(range(2,8,2))
print(even_nos)
squares = []
for value in range(1,11):
	square = value**2													#squaring a number
	squares.append(square)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
