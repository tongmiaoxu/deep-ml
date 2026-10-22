def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if not a or not b or any(len(row) != len(b) for row in a):
		return -1
	c = []
	for j in range(0,len(a)):
		c_1 = 0
		for i in range(0,len(b)):
			c_1 += b[i]*a[j][i] 
		c.append(c_1)
	return c
