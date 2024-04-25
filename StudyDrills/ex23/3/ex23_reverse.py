import sys

script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
  

def print_line(line, encoding, errors):
    next_lang = line.strip().decode(encoding, errors=errors)
    cooked_string = next_lang.encode(encoding, errors=errors)

    print(cooked_string, b'<===>', next_lang)


languages = open('simple_encoding.txt', mode='rb')  # open file in binary mode

main(languages, input_encoding, error)
