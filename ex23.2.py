

import sys
scipt, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        #print("debug if line in main..............")
        print_line(line,encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    #print("debug print_line function call............***********")
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<=======================>", cooked_string)

languages = open("languages2.txt", encoding ="utf-8")

main(languages, input_encoding, error)
