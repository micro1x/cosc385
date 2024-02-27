import numpy 

lst = numpy.array([int(i) for i in range(99) if str(2**i)[-1] == "6"])

print(lst)