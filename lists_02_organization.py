cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()										#sort the list (original sequence of elements is lost)
print(cars)
cars.sort(reverse=True)							#sort the list in reverse order(original sequence is lost)
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)										#original sequence
print(sorted(cars))								#string sort, original sequence is not lost
print(cars)										#original string
cars.reverse()
print(cars)
print(len(cars))
