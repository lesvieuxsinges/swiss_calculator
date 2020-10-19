import functions

class Fraction:

	def __init__(self, top, bottom):

		if bottom == 0:	#error divison by zero
			raise ValueError('This fraction\'s gonna give you an infinite result, not sure that\'s what you are looking for... \n b=0 in a/b')
		self.top, self.bottom = functions.simpfrac(top, bottom)
		if self.bottom<0:
			self.bottom=-self.bottom
			self.top=-self.top


	def __add__(self, stranger):
		result=Fraction(1,1)
		if type(stranger) == int:
			result.top = self.top + self.bottom*stranger
			result.bottom = self.bottom

		elif type(stranger) == Fraction:
			result.top = self.top*stranger.bottom+stranger.top*self.bottom
			result.bottom = self.bottom * stranger.bottom

		result.top, result.bottom = functions.simpfrac(result.top, result.bottom)
		return str(result)


	def __mul__(self, stranger):
		result=Fraction(1,1)
		if type(stranger) == int:
			result.top = self.top * stranger
			result.bottom = self.bottom

		elif type(stranger) == Fraction:
			result.top = self.top * stranger.top
			result.bottom = self.bottom * stranger.bottom
		return (str(result))


	def __truediv__(self, stranger):
		result = Fraction(1,1)
		if type(stranger) == Fraction:
			result.top = self.top * stranger.bottom
			result.bottom = self.bottom * stranger.top

		if type(stranger) == int:
			result.bottom = self.bottom * stranger
			result.top = self.top
		result.top, result.bottom = functions.simpfrac(result.top, result.bottom)
		return str(result)


	def __sub__(self, stranger):
		result = Fraction(1,1)
		if type(stranger) == int:
			result.top = self.top+self.bottom*stranger
			result.bottom = self.bottom

		elif type(stranger) == Fraction:
			result.top = self.top*stranger.bottom-stranger.top*self.bottom
			result.bottom = self.bottom * stranger.bottom

		result.top, result.bottom = functions.simpfrac(result.top, result.bottom)
		return str(result)


	def __str__(self):
		if self.top != 0 and self.bottom != 0 and self.bottom != 1:  #and self.bottom !=-1#:
			return('{}/{}'.format(self.top,self.bottom))
		elif self.top == 0:
			return('0')
		elif self.bottom == 1:
			return('{}'.format(self.top))
#		elif self.bottom == -1:
#			return('-{}'.format(self.top))

	def __repr__(self):
		return(str(self))

	def __radd__(self, stranger):
		return(self+stranger)
	def __rsub__(self, stranger):
		return(Fraction(stranger*self.bottom-self.top, self.bottom))
	def __rmul__(self, stranger):
		return(self*stranger)
	def __rtruediv__(self, stranger):
		return(Fraction(stranger*self.bottom, self.top))

	def __eq__(self, stranger):
		if type(stranger) == int:
			stranger = Fraction(stranger,1)
		return (self.top/self.bottom) == (stranger.top/stranger.bottom)

	def __ne__(self, stranger):
		if type(stranger) == int:
			stranger = Fraction(stranger,1)
		return (self.top/self.bottom) != (stranger.top/stranger.bottom)

	def __lt__(self, stranger):
		if type(stranger) == int:
			stranger = Fraction(stranger,1)
		return (self.top/self.bottom) < (stranger.top/stranger.bottom)

	def __gt__(self, stranger):
		if type(stranger) == int:
			stranger = Fraction(stranger,1)
		return (self.top/self.bottom) > (stranger.top/stranger.bottom)

	def __le__(self, stranger):
		if type(stranger) == int:
			stranger = Fraction(stranger,1)
		return (self.top/self.bottom) <= (stranger.top/stranger.bottom)

	def __ge__(self, stranger):
		if type(stranger) == int:
			stranger = Fraction(stranger,1)
		return (self.top/self.bottom) >= (stranger.top/stranger.bottom)


if __name__ == "__main__":
	print(Fraction(int(input()), int(input())))
