import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
	print(">>>>>>>> main", repr(language_file), encoding, errors)
	line = language_file.readline()

	if line:
		print(">> There is a line", repr(line))
		print_line(line, encoding, errors)
		print(">> calling main again")
		return main(language_file, encoding, errors) # goto line 5
	print("<<<<<<<<<<<<< exit main")

		# calling main inside main -- if you can do one thing, you can do it with another
		# can call any function while in a function
		#

def print_line(line, encoding, errors):
	print(">>>>>>>>", repr(line), encoding, errors)
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors) # do special settings,
	#sets error parameter default in none added in sys.argv
	cooked_string = raw_bytes.decode(encoding, errors=errors)

	print(raw_bytes, "<============>", cooked_string)
	print("Exit >>>>print line")

languages = open("languages2.txt", encoding = "utf-8")

main(languages, input_encoding, error)

#Dee Bes = decode bytes, encode strings
