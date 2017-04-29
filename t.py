def decode(letters, numbers):
	secret_message = ''
	for i in numbers:
		secret_message += letters[i]
	print secret_message

def main():
	letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.']
	numbers = [
		2,(7+7),(26/2),(20-1),0,2,(2*10-1),(13*2),12,4,((5+5+3)*2),8,5,(13*2),((4*2)*(2+1)),(7*2),20,26,0,(10+7),4,((20+6)/2)*2,8,((20+6)/2),19,4,(20-3),4,18,19,4,3,(9*3)
	]
	decode(letters, numbers)

if __name__ == "__main__":
	main()