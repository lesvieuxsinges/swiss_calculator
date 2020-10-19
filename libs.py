#FILE DEFINING BASIC FUNCTIONS FOR ALL OF MY PROGRAMS
from fraction import *
#FUNCTION N°0: sums terms of a function

def summ(x):
	ret=0
	for i in x:
		ret+=i
	return(ret)
#FUNCTION N°1:	this function splits an expression into its terms

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
	return x


#FUNCTION N°2:	this function multiplies every elements of a list together

def mult(x):
	product=1
	for i in x:
		product *= i

	return product


#FUNCTION N°3:	this function creates a list of d primes numbers
def fp(d):
	old=new=[2]							#old and new are the variables used to stock the prime numbers
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


#FUNCTION N°4:	this function splits a number into its prime factors

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


#FUNCTION N°4:	this function simplifies a square root into a*sqrt(b) where a and b are prime numbers

def sqrtsimp(x):

	remanantx, x,osqrt,isqrt=x, decomp(x)+[1],1,1		#osqrt is for out of the squart root, and isqrt for in (ex: sqrt(12)=2sqrt(3),hence 2 is out and three in)

	for i in range(len(x)-1):			#taking all the prime factors of the number to simplify
		if x[i]==x[i+1]:			#if there is a square number
			osqrt*=x[i]			#extract it from the root and multiply it, and we 'neutralize' the other one
			x[i+1]=1
		else:
			isqrt*=x[i]		#if it is not a square, let it in the root, and multiply it with the precedents

	return["sqrt("+str(remanantx)+')='+str(osqrt)+'sqrt('+str(isqrt)+')',osqrt,isqrt]


#FUNCTION N°5: this function simplifies a fraction
def simpfrac(top,bottom):

		top, bottom = decomp(top), decomp(bottom)
		for i in top:
			for j in bottom:
				if i==j:
					top.remove(i)
					bottom.remove(j)


#FUNCTION N°6: this function returns the solution for a first degree equation
#needs not use of fractions
def esolve(eq):

	eq=cut.sumsplit(eq) #splits a sum into its terms into a list

	#defining the a and b for ax+b=0
	a,b=[],[]
	#If there's only one x, we are obviously kindly precising it to the program
	for i in range(len(eq)):
		if eq[i]=='x':
			eq[i]='1x'
	#if we want to use the coefficients, for a sign table for example, this is useful
	coeff=[]
	for i in eq:

		#if it is ax, then adding all the a together
		if 'x' in i:
			i=i[:i.index('x')]+i[i.index('x')+1:]
			a.append(fraction.Fraction(int(i),1))
			coeff.append(fraction.Fraction(i,1))

		#if it is a b alone, then adding all the b together
		else:
			b.append(fraction.Fraction(i,1))
	return(fraction.Fraction(-sum(b)/sum(a)),coeff)
