class SlidingPuzzle:
	def __init__(self,numRows,numColumns):
		self.numRows=numRows
		self.numColumns=numColumns
		self.__listNumbers=[]
		acc=0
		for row in range(0,self.numRows):
			self.__listNumbers.append([])
			for column in range(0,self.numColumns):
				self.__listNumbers[row].append(acc)
				acc+=1
		print(self.__listNumbers)

		
	def displayPuzzle(self):
		puzzle=''
		for row in range(self.numRows):
			for column in range(self.numColumns):
				if self.__listNumbers[row][column]>=10:
					puzzle+=str(self.__listNumbers[row][column])+' '
				else:
					puzzle+=str(self.__listNumbers[row][column])+'  '
				
			print(puzzle)
			puzzle=''
		
def main():
	board=SlidingPuzzle(3,4)
	board.displayPuzzle()
	
	
	
main()