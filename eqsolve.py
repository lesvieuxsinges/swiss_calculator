#This program solves equations of the first degree. Warning! Putting multiple X will result in an error, because of the conversions
import libs
import fraction
import cut

def esolve(eq):

	eq=cut.sumsplit(eq) #splits a sum into its terms into a list

	#defining the a and b for ax+b=0
	a,b=[],[]
	#If there's only one x, we are obviously kindly precising it to the program
	for i in range(len(eq)):
		if eq[i]=='x':
			eq[i]='1x'
		elif eq[i]=='-x':
			eq[i]='-1x'
	#if we want to use the coefficients, for a sign table for example, this is useful
	coeff=[]
	print(eq)
	for i in eq:

		#if it is ax, then adding all the a together
		if 'x' in i:
			i=i[:i.index('x')]
			a.append(int(i))
			coeff.append(int(i))
			print('a', a, '\ncoeff', coeff, '\ni', i)

		#if it is a b alone, then adding all the b together
		else:
			b.append(int(i))
			print('b', b)
	result = fraction.Fraction(libs.summ(b), libs.summ(a))*(-1)
	print(result)
	print("libssummb",libs.summ(b),"\nlibssuma", libs.summ(a))
	return(result, libs.summ(coeff))

if __name__ == "__main__":
	print(esolve(input('give a first degree expression >>>')))
