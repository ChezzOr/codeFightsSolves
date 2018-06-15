def reverseParentheses(s):
   	return recursiveParenthesis(s)
    
def innerRecursion(input):
	while input.find('(') != -1:
		input = input[:input.find('(')] + innerRecursion(input[input.find('(') + 1:])
	shifts = input[:input.find(')')]
	shifts = shifts[::-1]
	return shifts + input[input.find(')') + 1:]

def recursiveParenthesis(input):
	while input.find('(') != -1:
		input = input[:input.find('(')] + innerRecursion(input[input.find('(') + 1:])
	return input

def testCases():
	print(reverseParentheses('a(bc)de'))
	print(reverseParentheses('a(bcdefghijkl(mno)p)q'))
	
if __name__ == '__main__':
	testCases()
