def name():
	print("who are you")
	name = input()
	print(F"hello ,{name}!")
#main for the file it runs only when this files runs
def main():
	print("what's your favorite number")
	num = input()
	print(F"wow mine too is  ,{num}!")
#when  you run this file, it will not run either functions, to do so
if __name__ == '__main__':
	main()