def squares(length):
    for n in range(length):
        yield n ** 2

for square in squares(4):
    print(square)

# Instead of creating a list and keeping the whole sequence in the memory, the generator generates the next element in demand.
def generator():
    t = 1
    print ('First result is ',t)
    yield t
 
    t += 1
    print ('Second result is ',t)
    yield t
 
    t += 1
    print('Third result is ',t)
    yield t
 
call = generator()
next(call)
next(call)
next(call)