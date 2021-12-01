import numpy

B = numpy.array([3, 1, 2, 2])
A = numpy.array([[1, 2, 2], [9, 7, 8], [9, 4, 3], [6, 0, 7], ])

print(A)
x = []

ar = A[0:2, 0]
br = numpy.array([A[0][1], A[0][2]])
print(br)
x.append(numpy.concatenate((ar, br)))
x.append(numpy.concatenate((ar, br)))
x = numpy.array(x)
print(x)
