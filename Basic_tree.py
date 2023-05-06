# your code goes here

class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.val = data
	
	def inorder(self):
		print('Inside - ')
		if self.left:
			print(self.left.val)
		print(self.val)
		if self.right:
			print(self.right.val)
			
	def check(self):
		if self == root:
			print('Yes', root.val)
		else:
			print('No')
		print(self is root)	
		
if __name__ == "__main__":
	print('Hello')
	root = Node(5)
	root.left = Node(4)
	root.right = Node(6)
	root.inorder()
	root.check()
