from sys import argv

# These are the values that are used to convert back and forth between Regular text and Leet speak
# NOTE: This script only supports a one to one relationship and will fail to convert from leet speak if not configured as such
alpha = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numer = ['_', 'A', 'B', 'C', 'D', '3', 'F', '6', '4', '1', 'J', 'K', 'L', 'M', 'N', '0', 'P', 'Q', 'R', '5', '7', 'U', 'V', 'W', 'X', 'Y', 'Z']

# main function for the script
def main():
	# print(len(argv), argv)
	# first check the that arguments have been given
	if len(argv) < 1:
		print('ERROR: No arguments given')
		print('Please provide either a file name or string to be converted')
		get_usage()
	# check if the user has asked to see the usage
	elif '-h' in argv:
		get_usage()
	# check if the user has specified a valid conversion options
	elif '-d' not in argv and '-c' not in argv:
		print('ERROR: incorrect options specified')
		print('Please specify one option')
		get_usage()
	# if the user has everything correct, then
	elif len(argv) > 0:
		index = len(argv)
		last_index = argv[index-1]

		# if user has specified just -c
		if '-c' in argv and '-d' not in argv:
			print(get_converted(last_index))
		# if user has specified just -d
		elif '-d' in argv and '-c' not in argv:
			print(get_convert_from(last_index))
		# two options have been specified
		else:
			print('ERROR: incorrect options specified')
			print('Please specify one option')
			get_usage()

# This function converts strings from regular text to leet_speak
# And returns the result
def get_converted(string):
	result = ''
	# Enumerate through the string
	for i,v in enumerate(string):
		# Standardise the input to uppercase
		v = v.upper()
		# If letter exists in the alpha array, convert it
		if v in alpha:
			index = alpha.index(v)
			result += numer[index]
		# Otherwise ignore it
		else:
			result += v

	# Return the result
	return result

# This function converts string from leet_speak to regular text
# And return the result
def get_convert_from(string):
	result = ''
	# Enumerate through the string
	for i,v in enumerate(string):
		# Standardise the input to uppercase
		v = v.upper()
		# If value exists in the numer array, convert it
		if v in numer:
			index = numer.index(v)
			result += alpha[index]
		# Otherwise ignore it
		else:
			result += v

	# Return the result
	return result

# this prints the usage for the script out to the screen
def get_usage():
		print('\nUSAGE: python3 l33t_speak.py [option] [string | filename]\n')
		print('OPTIONS: ')
		print('-c\tConvert from regular text to leet speak')
		print('-d\tConvert from leet speak to regular text')
		print('-h\tDisplay the usage of this script')
		print('\nEG:')
		print('\tpython3 l33t_speak.py -c hello')
		print('\tpython3 l33t_speak.py -d 43110')
		print('\tpython3 l33t_speak.py -c text.txt')
		print('\nCOMMON ISSUES:')
		print('\t- W.I.P.: converting files has not been implemented yet')
		print('\t- If [String | Filenme] contains spaces, surround with quotes')
		print('\t- Make sure the string or filename is always the last argument')
		return 'prints out to console'

# If script is imported or not
if __name__ == '__main__':
	main()
else:
	print('Successfully imported l33t_speak.py')
	print('NOTE: converting files has not yet been implemented.')
	print('Visit URL for more projects')
	print()
	main()