#The Karplus-Strong Algorithm 

import numpy as np

def ks_loop(x, alpha, D):
	"""
	As length of output signal greater than input signal, 
	D must be larger than 1
	"""
	if D<1:
		print "Duration D must be greater than 1"
		return None

	#x is an input signal, and hence must be a row vector
	if x.ndim!=1:
		print ('Wrong array size of imput signal. Should be a row vector')
		return None

	#M = number of input samples
	M = len(x)

	#N - Number of output samples
	#y is the output signal
	size_y = D*M

	#Initiatlize y with random input
	y = np.zeros((size_y, 1))
	for i in range(M):
		y[i] = x[i]

	for j in range(M, size_y):
		y[j] = float(alpha*y[j-M])

	return y


#Matrix Implementation of Karplus-Strong Algorithm
def ks_matrix(z, alpha, D):
	if D<1:
		print "Duration D must be greater than 1"
		return None

	#x is an input signal, and hence must be a row vector
	if x.ndim!=1:
		print ('Wrong array size of imput signal. Should be a row vector')
		return None

	M = len(x)

	#Create a vector with powers of alpha
	a = np.ones((1,D))
	b = np.arange(D)	//[0, 1, 2, 3...., D-1]
	alphaVector = pow(a,b)

	#Create a matrix with all columns being powers of alpha
	alphaMatrix = np.eye(D,M)
	for index in range(M):
		alphaMatrix[:, index] = alphaVector

	xMatrix = np.tile(x, (D,1))

	yMatrix = alphaMatrix * xMatrix

	y = yMatrix.flatten()

	return y