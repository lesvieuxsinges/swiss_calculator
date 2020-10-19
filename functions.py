#preface i am a feignant, so i am using a function to multiply every elements of a list
def mult(x):
	product=1
	for i in x:
		product *= i

	return product


#FIRST FUNCTION: ADD ir PRIMES NUMBERS TO A LIST
#c is the number which is used to verify that the potential prime number is one or not, and a is the incrementator of space between each prime number, b is the verification divisor and the iterations count
#old and new are the variables used to stock the prime numbers
def fp(d):
	old=new=[2]
	for b in range (d): 						#number of primes numbers we want
		a=0	 						#subtility of the program: having an useless turn allows us to define c only in the code, which is more elegant

		while len(new)==len(old):
			for b in old:
				if (old[-1]+a)/b == int((old[-1]+a)/b): #verifying that the new number will be prime and not a random number
					c=1
					break 				#after one false verification, we can quit

			if c==0:
				new=new+[old[-1]+a]			#adding new prime number
			a+=1
			c=0 						#"cleaning" the precedent non prime number verification

		old=new
	return new

#SECOND FUNCTION: decomposes a number into his prime factors
def decomp(n):
#	n=int(n)
	if n<0:
		caca=-1
		n=-n
	elif n==0:
		return([0])
	else:
		caca=1
	fps,a,copy,p=[],0,n,1				#init variables, fps=result/primes factors, a is just the incrementor of potentials fps, and p is the product of the fps
	pn=fp(1)

	while n>p:					#while the product of prime factors is not n

		while copy/pn[a]==int(copy/pn[a]):	#used for put the right number of prime facotrs (ex:2*2=4)
			fps.append(pn[a])
			copy=copy/pn[a]			#divising the copy to reuse it, it is every time the futur number to divise

		pn=fp(len(pn))
		a+=1
		p=1

		for b in range(len(fps)):p=p*fps[b]	#making the product of the prime factors
	if caca==-1:
		return [caca]+fps
	else:
		return fps

#THIRD FUNCTION: simplifies a square root into a*sqrt(b) where a and b are prime numbers
def sqrtsimp(x):

	remanantx, x,osqrt,isqrt=x, decomp(x)+[1],1,1		#osqrt is for out of the squart root, and isqrt for in (ex: sqrt(12)=2sqrt(3),hence 2 is out and three in)

	for i in range(len(x)-1):			#taking all the prime factors of the number to simplify
		if x[i]==x[i+1]:			#if there is a square number
			osqrt*=x[i]			#extract it from the root and multiply it, and we 'neutralize' the other one
			x[i+1]=1
		else:
			isqrt*=x[i]		#if it is not a square, let it in the root, and multiply it with the precedents

	return["sqrt("+str(remanantx)+')='+str(osqrt)+'sqrt('+str(isqrt)+')',osqrt,isqrt]

def simpfrac(top,bottom):

		top, bottom = decomp(top), decomp(bottom)
		for i in top:
			for j in bottom:
				if i==j:
					top.remove(i)
					bottom.remove(j)
					break
				break
		top, bottom = mult(top), mult(bottom)
		return top, bottom
