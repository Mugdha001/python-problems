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
print(min(squares))														#minimum number in list
print(max(squares))														#maximum number in list
print(sum(squares))														#sum of all numbers in list

#list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)
numbers=[value for value in range(1,20,2)]
print(numbers)

#list slicing
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])														#list items 0,1,2
print(players[1:4])														#list items 1,2,3
print(players[:4])														#list items 0,1,2,3
print(players[2:])														#list items 2 and above
print(players[-3:])														#last 3 items of list	
print(players[:])														#all items												


#for loop list slicing
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

#storing a copy of list , different independent lists (when item appended to one list, it is not reflected in another list)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
players_copy= players[:]

#make full copy of a list (one list equals another list) when item is appended in one list it also reflects in another list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
players_copy= players

