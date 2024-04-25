import sys
script, input_encoding, error = sys.argv # New hanya ce ta importing argv a command line.


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
  
 
def print_line(line, encoding, errors):
    next_lang = line.strip() # Yana cire mana duk wani unessary \n.
    raw_bytes = next_lang.encode(encoding, errors=errors) # Yana maida chr zuwa bytes.
    cooked_string = raw_bytes.decode(encoding, errors=errors) # Yana maida bytes zuwa chr.

    print(raw_bytes, '<===>', cooked_string)


languages = open('languages.txt', encoding="utf-8") # kalar encoding dn d nake so.

main(languages, input_encoding, error)