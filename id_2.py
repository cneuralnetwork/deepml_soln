def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	r=len(a)
	c=len(a[0]) if r>0 else 0
	b=[[0 for _ in range(r)] for _ in range(c)]
	for i in range(r):
		for j in range(c):
			b[j][i]=a[i][j]
	return b
