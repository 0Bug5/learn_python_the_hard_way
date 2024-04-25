import sys

script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
  

def print_line(line, encoding, errors):
    # next_lang = line.strip().decode(encoding, errors=errors)
    cooked_string = line.encode(encoding, errors=errors)
    bugs = '0Bug5_H4ck3d_this_utf-8_:)'

    print(cooked_string, '<===>', bugs)


languages = open('simple_encoding.txt', encoding='utf-8')  # open file in binary mode

main(languages, input_encoding, error)
