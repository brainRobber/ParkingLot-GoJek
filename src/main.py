import sys
from input_parser import InputParser

def main():
	parser = InputParser()
	if len(sys.argv) == 1:
		print("Please enter 'exit' to quit")
		print("waiting for input ...")

		while True:
			try:
				input_string = raw_input()
				if input_string == "exit":
					break
				elif input_string is None:
					continue
				else:
					parser.parse_text_input(input_string.strip())
			except Exception as e:
				print(e)
	elif len(sys.argv) == 2:
		pass
	else:
		print("incorrect number of arguments")


if __name__ == '__main__': 
	main()