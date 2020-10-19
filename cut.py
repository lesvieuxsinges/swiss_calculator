#This program splits an expression into every terms of the sum.


def sumsplit(x):
	x=list(x)

	#this while adds a + before every -, so we can use the + to split it without losing data
	i=0
	while i < len(x):
		if x[i]=='-':
			x.insert(i, '+')
			i+=1
		i+=1
	x=''.join(x).split('+')
	for i in x:
		if i=='':
			x.remove('')
	return x

if __name__ == "__main__":
	print(sumsplit(input()))
