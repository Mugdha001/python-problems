number_a = 12
number_b = 13
print(number_a + number_b)											#adding two numbers
bicycles=["trek", "mountaineering", "tough", "universal"]			#create a list
print(bicycles[0].title())											#first element of list
print(bicycles[-1].title())											#last element of list
print("My first bicycle was a " + bicycles[0].title() + ".")
bicycles.append('ducati')											#append an element at the end of the list
bicycles.insert(0, 'honda')											#insert element at 0th position
del bicycles[1]														#delete 1st position 
print(bicycles)										
popped_bicycles = bicycles.pop()									#pop last item in bicycles
print(popped_bicycles)
print(bicycles.pop(0))												#pop first element in bicycles
bicycles.remove('mountaineering')									#remove based on name
print(bicycles)
